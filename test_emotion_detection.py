import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_emotion_detector(self):
        response = emotion_detector("I am glad this happened")

        self.assertIn("anger", response)
        self.assertIn("disgust", response)
        self.assertIn("fear", response)
        self.assertIn("joy", response)
        self.assertIn("sadness", response)

if __name__ == "__main__":
    unittest.main()
