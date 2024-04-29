# 创建一个学生数据表的程序,包括firtname,lastname,city,score,存储在dirctory中,然后存储在db中


# 连接mysql 数据库  mysql -u root -p 123456  #连接数据库
import mysql.connector

def connect_to_database():
    try:
        # 连接到 MySQL 数据库
        conn = mysql.connector.connect(
            host="localhost",
            user="OliviaWqq",
            password="123456",
            database="user_info_db"
        )
        print("成功连接到数据库")
        return conn
    except mysql.connector.Error as error:
        print("连接数据库时发生错误:", error)
        return None

def execute (conn, sql): #执行sql语句
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        print("执行成功")
    except mysql.connector.Error as error:
        print("执行SQL语句时发生错误:", error)
        conn.rollback() #回滚


def get_user_info(user_info_list: list):
    while True:
        student_info = input("请输入学生的信息（用逗号分隔，顺序为：firstname,lastname,city,score）：")
        student_info = student_info.strip()  # 去除输入字符串两端的空格
        student_info = student_info.split(",")  # 使用逗号分割输入字符串

        # 检查输入是否有效
        if len(student_info) != 4:
            print("输入无效，请按正确格式输入学生信息！")
            continue

        firstname, lastname, city, score = student_info
        # 将学生信息存储在字典中
        student = {
            'firstname': firstname,
            'lastname': lastname,
            'city': city,
            'score': float(score)
        }

        user_info_list.append(student)

         # 提示用户是否继续输入学生信息
        choice = input("是否继续输入学生信息？(y/n): ")
        if choice.lower() != 'y':
            break


def main():
    #调用
    usr_infos = []
    get_user_info(usr_infos)
    #遍历打印学生信息
    for usr_info in usr_infos:  # usr_info是字典类型
        print(usr_info)

    # todo:存储到db中
    conn = connect_to_database()
    if conn is not None:
        for usr_info in usr_infos:
            sql = "INSERT INTO user_info_db.user_info (firstname, lastname, city, score) VALUES (%s, %s, %s, %s)"
            values = (usr_info['firstname'], usr_info['lastname'], usr_info['city'], usr_info['score'])
            execute(conn, sql, values)
        conn.close()


if __name__ == '__main__':
    main()
