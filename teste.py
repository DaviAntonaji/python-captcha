
import random
from captcha.audio import AudioCaptcha
from captcha.image import ImageCaptcha

audio = AudioCaptcha()
image = ImageCaptcha()

strings = "1234567890"
length = 8

captcha_text = ''.join(random.choice(strings) for x in range(length))
print(captcha_text)
data = audio.generate(captcha_text)
audio.write(captcha_text, 'out.wav')

data = image.generate(captcha_text)
image.write(captcha_text, 'out.png')
