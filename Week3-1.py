
'''
في هذا الأسبوع لدينا تحديين:
**التحدي الأول**:
قومي بإنشاء ملف بآتوم باسم Week3-1.py
اكتبي لعبة تطبع اسم اللعبة أولاً
Numbers from 1 to 10
ثم تطلب من المستخدم أن يحزر الرقم
"Guess the number: "
إذا المستخدم لم يدخل الرقم الصحيح ستبقى اللعبة تسأله للأبد، إذا قام بإدخال الرقم الصحيح، يظهر للمستخدم:
"Great! You did it!"
لا تنسي أن تقومي بتخزين رقم من اختيارك ليكون هو الرقم الصحيح وتخزينه في متغير.
الرقم يجب أن يكون بين 1 و10
جربي الكود من خلال عمل run للملف على command prompt- terminal.
قومي برفع الملف هنا على الريبوريتوري ثم على GiHub، ثم املأي الاستمارة
https://forms.gle/ZQWDrPKkVgr4Dnmd6
ملاحظة:
آخر يوم للتسليم هو يوم الأحد القادم
'''

# print Name of Game

print('Numbers from 1 to 10')

# Insert variables

num=3
Numbers=[1,2,3,4,5,6,7,8,9,10]

# While loop

while True:
    num= float(input('Guess the number: '))
    if num in Numbers:
        print('Great! You did it!')
        break

    
