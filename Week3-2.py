'''
**التحدي الثاني**:
قومي بعمل ملف بآتوم باسم Week3-2.py
المطلوب بهذا التحدي كتابة برنامج يقوم بالطلب من المستخدم (الأهل أو المعلمة) بإدخال اسم الطالب٫ فيعيد اسم الطالب بالإضافة إلى مجموع علاماته.
*أرجو كتابة رسالة الطلب كما هي في الأسفل
Enter student's name
علامات الطلاب وأسماؤهم مخزنة بداخل القوائم التالية٬ أرجو نسخها كما هي:
s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]
ملاحظة:
إذا أدخل المستخدم اسم غير موجود ستظهر له ملاحظة بأن الاسم غير مسجل٫ والمجموع صفر
مثال:
Enter student's name: Ayamn
Student is not recorded 0
مثال ٢:
Enter student's name: Sami
Sami 96
قومي برفع الملف على الريبوريتوري ثم على GiHub، ثم املأي الاستمارة
https://forms.gle/Sd7QFNr9CLoXauzeA
ملاحظة:
آخر يوم للتسليم هو يوم الاثنين القادم
'''

# list
s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]
# Variables
Name=input("Enter student's name: ")
Sum=0
# for loop
for s in s1 or s2 or s3:
    if Name in s1:
        Sum=sum(s1[1:])

    elif Name in s2:
        Sum=sum(s2[1:])

    elif Name in s3:
        Sum=sum(s3[1:])

    else:
        Name='Student is not recorded'
# Print
print(Name, Sum)
