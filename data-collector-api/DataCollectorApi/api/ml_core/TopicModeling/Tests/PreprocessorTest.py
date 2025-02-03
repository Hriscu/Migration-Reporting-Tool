import unittest
from TopicModeling.preprocessor import Preprocessor


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.preprocessor = Preprocessor()

    def test_url_elimination_equal(self):
        input_text = "This is an amazing link: http://something.com and this one too https://example.org"
        expected_output = "This is an amazing link:  and this one too "
        self.assertEqual(self.preprocessor.url_elimination(input_text), expected_output)

    def test_url_elimination_not_equal(self):
        input_text = "This is an amazing link: http://something.com"
        expected_output = "This is an amazing link: http://something.com"
        self.assertNotEqual(self.preprocessor.url_elimination(input_text), expected_output)

    def test_hashtag_extraction_equal(self):
        input_text = "text with a #hashtag"
        output_text = "text with a hash tag"
        self.assertEqual(self.preprocessor.hashtag_extraction(input_text), output_text)

    def test_hashtag_extraction_not_equal(self):
        input_text = "text with a #hashtag"
        output_text = "text with a #hashtag"
        self.assertNotEqual(self.preprocessor.hashtag_extraction(input_text), output_text)

    def test_emoji_elimination_equal(self):
        input_text = "This is an emoji 👍"
        output_text = "This is an emoji "
        self.assertEqual(self.preprocessor.emoji_elimination(input_text), output_text)

    def test_emoji_elimination_not_equal(self):
        input_text = "This is an emoji 👍"
        output_text = "This is an emoji"
        self.assertNotEqual(self.preprocessor.emoji_elimination(input_text), output_text)

    def test_lowercase_equal(self):
        input_text = "This is a TEST"
        output_text = "this is a test"
        self.assertEqual(self.preprocessor.lowercase(input_text), output_text)

    def test_lowercase_not_equal(self):
        input_text = "This is a TEST"
        output_text = "this is a TEST"
        self.assertNotEqual(self.preprocessor.lowercase(input_text), output_text)

    def test_punctuation_elimination_equal(self):
        input_text = "Hello, world!"
        output_text = "Hello world"
        self.assertEqual(self.preprocessor.punctuation_elimination(input_text), output_text)

    def test_punctuation_elimination_not_equal(self):
        input_text = "Hello, world!"
        output_text = "Hello world!!!"
        self.assertNotEqual(self.preprocessor.punctuation_elimination(input_text), output_text)

    def test_expand_contraction_equal(self):
        input_text = "This can't be a test"
        output_text = "This cannot be a test"
        self.assertEqual(self.preprocessor.expand_contractions(input_text), output_text)

    def test_expand_contraction_not_equal(self):
        input_text = "This can't be a test"
        output_text = "This can't' be a test"
        self.assertNotEqual(self.preprocessor.expand_contractions(input_text), output_text)

    def test_lemmatization_equal(self):
        input_text = "The cats are running fast"
        output_text = "cat run fast"
        self.assertEqual(self.preprocessor.lemmatization(input_text), output_text)

    def test_lemmatization_not_equal(self):
        input_text = "The cats are running fast"
        output_text = "The cats are running fast"
        self.assertNotEqual(self.preprocessor.lemmatization(input_text), output_text)

    def test_preprocessing_pipeline(self):
        input_text = "I can't believe #AI is amazing 😍! Check this out: http://example.com"
        tokens = self.preprocessor.preprocessing_pipeline(input_text)
        self.assertIsInstance(tokens, list)
        self.assertIn("amazing", tokens)
        self.assertNotIn("http", tokens)

    def test_bigrams_trigrams(self):
        data = [["natural", "language", "processing", "is", "fun"],
                ["natural", "language", "is", "powerful"],
                ["I", "study", "natural", "language"],
                ["Something", "about", "natural", "language"],
                ["Another", "list", "with", "natural", "language"],
                ["natural", "language", "is", "cool"]]
        result = self.preprocessor.bigrams_trigrams(data, min_count=2, threshold=2)
        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(doc, list) for doc in result))

        self.assertIn("natural_language", result[0])

    def test_remove_frequent_words(self):
        data_trigram = [["data", "analysis", "is", "useful"], ["data", "is", "important"]]

        corpus, id2word = self.preprocessor.remove_frequent_words(data_trigram)

        self.assertIsNotNone(corpus)
        self.assertIsNotNone(id2word)

        frequent_words = ["data"]
        for doc in corpus:
            for word_id, _ in doc:
                self.assertNotIn(id2word[word_id], frequent_words)
