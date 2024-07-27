from sample_config import Config
class Development(Config):
    # get this values from the my.telegram.org
    APP_ID =  9671629
    API_HASH = "be5c84e9dc1ca0e2b53d54b71e575124"
    # the name to display in your alive message
    ALIVE_NAME = "bilal"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgresql://postgres:bilal2331@localhost:5432/bilal"
    # After cloning the repo and installing requirements do python3 telesetup.py an fill that value with this
    STRING_SESSION = "1ApWapzMBuyaKQH4Qt30XL-yz_FUUAb2_vimiyvv36UEhJO7wPCm89zvqP5bhwYwSL7RVrJkWUbq5synA4ZZ382nY4N-lC432XM-475-K8xrc1Npoypv6TLFJJfRbRfEKpOvAaUaAkvoGpN7MperQxZ5Xawrzk-rMXi7pYzMsAfKcuquvcIW0RCNjIDEAQZgSoFeyMGkawqgSRol7GE75B0vONxyOPzE8IuRR1klBt4OO6mur9ySJccmS1DWlAeTqopPmZdNJJLj-wtF4vAGWIHZO1svn7aAU-hkCELrlNK6p-9_AW2OrJd-wM_RgwLEjRa_8l3H_q2GTZPJ-W80aWqRi3PeDY2w="
    # create a new bot in @botfather and fill the following vales with bottoken and username respectively
    TG_BOT_TOKEN = "7121027327:AAEVE4wgyK0LKfH62OZ36dPbwknj-nPkvrs"
    # command handler
    COMMAND_HAND_LER = "."
    # sudo enter the id of sudo users userid's in that array
    SUDO_USERS = []
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
