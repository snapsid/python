text = "X-DSPAM-Confidence:    0.8475";
num=text.find('0')
a=text[num:num+6]
print(float(a))
