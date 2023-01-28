import boto3


class EmotionGetter:
    def __init__(self):
        self.client = client = boto3.client('rekognition')

    def get_emotions(self, photo):
        with open(photo, 'rb') as image:
            response = self.client.detect_faces(Image={'Bytes': image.read()}, Attributes=['ALL'])
            print(' - Requested face detection and analysis')
        if len(response) > 0:
            print(' - A face was detected')
        for item in response.get('FaceDetails'):
            face_emotion_confidence = 0
            face_emotion = None
            for emotion in item.get('Emotions'):
                if emotion.get('Confidence') >= face_emotion_confidence:
                    face_emotion_confidence = emotion['Confidence']
                    face_emotion = emotion.get('Type')
            return face_emotion, face_emotion_confidence



def main():
    emot = EmotionGetter()
    a, b = emot.get_emotions('./rekognition/current_image.png')
    print(a)
    print(b)

if __name__ == '__main__':
    main()