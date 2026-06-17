import unittest
from emotionDetection import emotion_detector

class TestDetection(unittest.TestCase):

    def test_joy(self):
        response = emotion_detector("I am so happy I am doing this.")
        self.assertEqual(response["dominant_emotion"], "joy")

    def test_anger(self):
        response = emotion_detector("I hate working long hours.")
        self.assertEqual(response["dominant_emotion"], "anger")

    def test_sadness(self):
        response = emotion_detector("I am feeling very sad.")
        self.assertEqual(response["dominant_emotion"], "sadness")

    def test_fear(self):
        response = emotion_detector("I am really afraid that this will happen.")
        self.assertEqual(response["dominant_emotion"], "fear")

    def test_disgust(self):
        response = emotion_detector("I am disgusted by this behavior.")
        self.assertEqual(response["dominant_emotion"], "disgust")


if __name__ == "__main__":
    unittest.main()