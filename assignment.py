class Info:
    def __init__(self,name,num,male):
        self.name=name
        self.num=num
        self.male=male

    def print_Info(self):
        print("이름은 {}, 전화번호는 {}, 성별은 {}입니다.".format(self.name,self.num,self.male))

Info_list=[]
while 1:
    name = input("이름을 입력하세요: ")
    if name == "그만":
        for info in Info_list:
            info.print_Info()
        break
    num = input("전화번호를 입력하세요: ")
    male = input("성별을 입력하세요(male이나 female로 작성해주세요) : ")
    if (male == 'male'):
        male == 'male'
    elif (male == 'female'):
        male == 'female'
    else:
        male=male.replace(male,'unknown')

    info = Info(name, num, male)
    Info_list.append(info)
    for info in Info_list:
        info.print_Info()
    print()