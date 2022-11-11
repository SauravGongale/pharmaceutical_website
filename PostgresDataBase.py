import string
import psycopg2

class mysqldatabse:

    def __init__(self,roll,ei,password):
        self.rollno=roll
        self.emailId=ei
        self.password=password

    hostname="localhost"
    database="pharma"
    username="mysql"
    psw="admin"
    post_id=5432

    def Open_conn(self):
        try:   
            conn=psycopg2.connect(
                    host=self.hostname,
                    dbname=self.database,
                    user =self.username,
                    password=self.psw,
                    port=self.post_id)
            return conn
        except Exception as error:
            print("Exception : "+error)

    def Create_table(self):
        try:
            conn=self.Open_conn()
            cur= conn.cursor()#to execute query
            createsignup="""CREATE TABLE IF NOT EXISTS tbladmin (`id` int NOT NULL AUTO_INCREMENT,
                              `email_id` varchar(100) DEFAULT NULL,
                              `uname` varchar(100) DEFAULT NULL,
                              `upass` varchar(100) DEFAULT NULL,
                              `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
                              `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                              PRIMARY KEY (`id`))"""
            createcaptcha="""CREATE TABLE IF NOT EXISTS tblcaptcha (`captcha` varchar(100) DEFAULT NULL)"""

            createtblcart="""CREATE TABLE IF NOT EXISTS tblcart (`id` int NOT NULL AUTO_INCREMENT,
                              `customer_id` int DEFAULT NULL,
                              `medicine_id` int DEFAULT NULL,
                              `medicine_mrp_price` double DEFAULT NULL,
                              `medicine_discount_price` double DEFAULT NULL,
                              `total_medicines_price` double DEFAULT NULL,
                              `quantity` int DEFAULT NULL,
                              `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
                              `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                              PRIMARY KEY (`id`))"""
            
            createcontact="""CREATE TABLE IF NOT EXISTS tblcontact (`contact_id` int NOT NULL AUTO_INCREMENT,
                              `name` varchar(200) DEFAULT NULL,
                              `email` varchar(100) DEFAULT NULL,
                              `mobile` varchar(100) DEFAULT NULL,
                              `subject` varchar(100) DEFAULT NULL,
                              `message` varchar(500) DEFAULT NULL,
                              `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
                              PRIMARY KEY (`contact_id`))"""

            createcustomer="""CREATE TABLE IF NOT EXISTS tblcustomer (`id` int NOT NULL AUTO_INCREMENT,
                              `full_name` varchar(100) DEFAULT NULL,
                              `email_id` varchar(100) DEFAULT NULL,
                              `mobile_no` varchar(100) DEFAULT NULL,
                              `gender` varchar(45) DEFAULT NULL,
                              `address` varchar(400) DEFAULT NULL,
                              `pincode` varchar(100) DEFAULT NULL,
                              `uname` varchar(100) DEFAULT NULL,
                              `upass` varchar(100) DEFAULT NULL,
                              `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
                              `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                              PRIMARY KEY (`id`)"""

            createmedicine="""CREATE TABLE IF NOT EXISTS tblmedicine (`id` int NOT NULL AUTO_INCREMENT,
                              `medicine_name` varchar(100) DEFAULT NULL,
                              `medicine_type` varchar(100) DEFAULT NULL,
                              `medicine_description` varchar(900) DEFAULT NULL,
                              `medicine_image_name` varchar(200) DEFAULT NULL,
                              `medicine_image` varchar(400) DEFAULT NULL,
                              `medicine_mrp_price` double DEFAULT NULL,
                              `medicine_discount_price` double DEFAULT NULL,
                              `medicine_quantity` int DEFAULT NULL,
                              `medicine_manufacturing_date` varchar(100) DEFAULT NULL,
                              `medicine_expiry_date` varchar(100) DEFAULT NULL,
                              `medicine_status` varchar(45) DEFAULT NULL,
                              `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
                              `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                              PRIMARY KEY (`id`))"""

            createorder="""CREATE TABLE IF NOT EXISTS tblcaptcha (  `id` int NOT NULL AUTO_INCREMENT,
                              `order_no` int DEFAULT NULL,
                              `customer_name` varchar(100) DEFAULT NULL,
                              `email_id` varchar(100) DEFAULT NULL,
                              `mobile_no` varchar(100) DEFAULT NULL,
                              `address` varchar(400) DEFAULT NULL,
                              `pincode` varchar(100) DEFAULT NULL,
                              `medicine_image_name` varchar(200) DEFAULT NULL,
                              `medicine_name` varchar(200) DEFAULT NULL,
                              `quantity` int DEFAULT NULL,
                              `medicine_mrp_price` double DEFAULT NULL,
                              `medicine_discount_price` double DEFAULT NULL,
                              `medicine_total_price` double DEFAULT NULL,
                              `medicine_order_status` varchar(45) DEFAULT NULL,
                              `payment_mode` varchar(45) DEFAULT NULL,
                              `payment_id` int DEFAULT NULL,
                              `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
                              `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                              PRIMARY KEY (`id`))"""                              

            cur.execute(createsignup)
            cur.execute(createcaptcha)
            cur.execute(createtblcart)
            cur.execute(createcontact)
            cur.execute(createmedicine)
            cur.execute(createorder)
            conn.commit()   
            print("table created")
        except Exception as error:
            print("Exception : "+str(error))
        finally:
            print("Connection close")
            cur.close()
            conn.close()    

    def Insert_signup(self):
        flag =1
        try:
            conn=self.Open_conn()
            cur=conn.cursor()
            insertquery="""insert into  Signup_Data(RollNo,EmailId,Password)
                                values('"""+str(self.rollno)+"""',
                                '"""+self.emailId+"""','"""+self.password+"""');""" 
            cur.execute(insertquery)
            conn.commit()
        except Exception as error:
            flag =0
            print("Exception : "+str(error))
        finally:
            return flag
            print("Connection close")
            cur.close()
            conn.close()

class lgndb:
    hostname="localhost"
    database="pharma"
    username="mysql"
    psw="admin"
    post_id=5432
    def Open_conn(self):
        try:   
            conn=psycopg2.connect(
                    host=self.hostname,
                    dbname=self.database,
                    user =self.username,
                    password=self.psw,
                    port=self.post_id)
            return conn
        except psycopg2.Error as error:
            print("Exception : "+error)

    def insertToLgn(self,rollno,password):
        try:
            conn = self.Open_conn()
            cur= conn.cursor()
            select_query="""select RollNo,Password from Signup_Data"""
    
            cur.execute(select_query)
            result = cur.fetchall()

            
            for row in result:
                if(rollno==row[0] and password==row[1]):
                    query = """insert into Login_Data (RollNo,Password) values
                                ('"""+rollno+"""','"""+password+"""')"""
                    cur.execute(query)
                    conn.commit()
                    cur.close()
                    conn.close()
                    return True
            return False
        except psycopg2.Error as error:
                print(str(error))


 
        
            

