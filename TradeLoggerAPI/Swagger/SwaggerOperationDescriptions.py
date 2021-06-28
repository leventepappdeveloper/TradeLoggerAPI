def getRegisterUserOpDesc():
    return "Performs TradeLogger User Registration. Please note that the provided username and email values must be " \
           "unique."

def getLoginUserOpDesc():
    return "Performs TradeLogger User Authentication. Provide a valid Username-Password combination " \
            "corresponding to a registered TradeLogger User. Upon successful login, copy and paste " \
            "the authentication token into the \"Authorize\" value field as described in the " \
            "\"CONFIGURATION STEPS\" above."

def getUnregisterUserOpDesc():
    return "Unregisters the authenticated user from TradeLogger. Subsequent calls to API endpoints requiring " \
           "an authenticated user will fail."

def getCreateTradingAccountOpDesc():
    return "Creates a new trading account for the authenticated user. Please note that the same " \
           "user cannot have two trading accounts with the same name."

def getDeleteTradingAccountOpDesc():
    return "Removes the authenticated user's trading account with the account name specified in " \
           "the request body."

def getGetTradingAccountInfoOpDesc():
    return "Gets info on the authenticated user's trading account with the account name specified in the query string."

def getOpenShortIronCondorOpDesc():
    return "Opens a new short iron condor options trade in the specified trading account."