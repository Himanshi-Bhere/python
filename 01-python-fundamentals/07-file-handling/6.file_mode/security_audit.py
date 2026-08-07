with open("audit_log.txt", "a") as file:
    file.writelines([
        "User : Rahul\n",
        "login successfully\n\n",
        
        "User : Sara\n",
        "login Failed\n\n",
        
        "User : Himanshi\n",
        "Password changed\n\n"
    ])
