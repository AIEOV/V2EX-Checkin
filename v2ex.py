
        main()
        print("----------V2EX签到执行完毕----------")
        pushtg(result)

def main_handler(event, context):
    if cookie:
        print("----------V2EX开始尝试签到----------")
        main()
        print("----------V2EX签到执行完毕----------")
        pushtg(result)
