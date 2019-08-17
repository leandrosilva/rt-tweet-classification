from sklearn.feature_extraction.text import CountVectorizer
from classifier import *
from sys_helpers import exit_if_error, wait_for_crl_c
from kafka_helpers import KAFKA_TWEET_TOPIC, get_kafka_hosts, create_kafka_consumer


print("Loading pre-trained model...")
(vocabulary, err) = load_vocabulary()
exit_if_error(err)

count_vect = CountVectorizer(vocabulary=vocabulary)
count_vect._validate_vocabulary()

(model, err) = load_model()
exit_if_error(err)

tfidf_transformer = tf_idf(DEFAULT_CATEGORIES)[0]


print("Connecting to consume Kafka stream...")
(consumer, err) = create_kafka_consumer(KAFKA_TWEET_TOPIC, get_kafka_hosts())
exit_if_error(err)


print("Ready to make predictions...")
wait_for_crl_c()

for message in consumer:    
    msg = message.value.decode("utf-8")

    X_new_counts = count_vect.transform([msg])
    X_new_tfidf = tfidf_transformer.transform(X_new_counts)

    predicted = model.predict(X_new_tfidf)
    predicted_label = fetch_train_dataset(DEFAULT_CATEGORIES).target_names[predicted[0]]

    print("[", predicted_label, "] =>", msg)
