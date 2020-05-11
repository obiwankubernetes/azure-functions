# Dependencies
    # An Azure account 
        # use cmd az login to log into acct
    # Python 3.6 and 3.7 require Azure Functions Core Tools version 2.7.1846 or a later 2.x version. Python 3.8 requires version 3.x of the Core Tools.
        # install node.js (npm included), put it in environment path, check node --version & npm --version, then use cmd npm install -g azure-functions-core-tools@3
    # The Azure CLI version 2.4 or later.
    # Python 3.8 (64-bit), Python 3.7 (64-bit), Python 3.6 (64-bit), which are supported by Azure Functions.


# create and activate venv

# create local function project directory and tunnel into it
    # func init LocalFunctionProj --python
    # cd LocalFunctionProj

# create a new function with name HTTP example and template HTTP trigger
       # func new --name HttpExample --template "HTTP trigger"

# run function locally
    # func start

# to get function to work, go to local host example given in output and append "name" from __init_py file at end 
    #   http://localhost:7071/api/HttpExample?name=Azure%20Rokstar

# stop local running function 
    #  by hitting ctrl + c

# create azure resources
    # create new resource group: az group create --name AzureFunctionsQuickstart-rg --location eastus
    # create storage account to attach to function: az storage account create --name funcqkstrtstorage --location eastus --resource-group AzureFunctionsQuickstart-rg --sku Standard_LRS
    # create function resource: az functionapp create --resource-group AzureFunctionsQuickstart-rg --os-type Linux --consumption-plan-location eastus --runtime python --runtime-version 3.8 --functions-version 3 --name QuickStartHttpExample --storage-account funcqkstrtstorage

# deploy the function
    # func azure functionapp publish QuickStartHttpExample

# find invoke url at bottom of output, appened name="name" to the end to invoke the HTTP trigger and get result of function