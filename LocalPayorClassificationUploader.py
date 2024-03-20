import requests
import uuid

# Authentication token (anonymized)
auth_token = 'your_auth_token_here'

# API endpoint URL
URL = 'https://prod.capturerx.com/apiservice/cumulus/v1/payor_classifications/'

# List of payor classifications with anonymized data
payor_classifications = [
    {
        'group': 'CRH01',
        'bin': '003585',
        'pcn': 'ASPROD1',
        'copayAmount': '3.00',
        'coveredEntityId': 'your_covered_entity_id_here',
        'effectiveDate': '2019-04-15',
        'isApproved': 'True',
        'isGroupIgnore': 'False',
        'isPayorMatched': 'False',
        'isPcnIgnore': 'False',
        'operatorId': 'your_operator_id_here',
        'planId': 'your_plan_id_here',
        'planName': 'MCO 20',
        'planTypeId': 'your_plan_type_id_here',
        'stateId': 'your_state_id_here',
        'terminationDate': 'None'
    },
    {
        'group': 'VNS03',
        'bin': '003585',
        'pcn': 'ASPROD1',
        'copayAmount': '3.00',
        'coveredEntityId': 'your_covered_entity_id_here',
        'effectiveDate': '2019-04-15',
        'isApproved': 'True',
        'isGroupIgnore': 'False',
        'isPayorMatched': 'False',
        'isPcnIgnore': 'False',
        'operatorId': 'your_operator_id_here',
        'planId': 'your_plan_id_here',
        'planName': 'MCO 20',
        'planTypeId': 'your_plan_type_id_here',
        'stateId': 'your_state_id_here',
        'terminationDate': 'None'
    }
]

# Headers for authentication
header = {'Authorization': 'Bearer ' + auth_token}

# List to store failed mappings
failures = []

# Iterate over payor classifications
for payor_classification in payor_classifications:
    # Generate a unique ID for each entry
    guid = str(uuid.uuid4())
    
    # Construct the request body
    body = {
        'id': guid,
        'group': payor_classification['group'],
        'bin': payor_classification['bin'],
        'pcn': payor_classification['pcn'],
        'contractId': None,
        'copayAmount': payor_classification['copayAmount'],
        'coveredEntityId': payor_classification['coveredEntityId'],
        'effectiveDate': payor_classification['effectiveDate'],
        'isApproved': payor_classification['isApproved'],
        'isGroupIgnore': payor_classification['isGroupIgnore'],
        'isLocal': True,
        'isPayorMatched': payor_classification['isPayorMatched'],
        'isPcnIgnore': payor_classification['isPcnIgnore'],
        'operatorId': payor_classification['operatorId'],
        'pharmacyChainId': None,
        'planId': payor_classification['planId'],
        'planName': payor_classification['planName'],
        'planTypeId': payor_classification['planTypeId'],
        'stateId': payor_classification['stateId'],
        'terminationDate': None
    }
    
    # Make the API request
    response = requests.post(URL, json=body, headers=header)
    
    # Print response status and text
    print(response)
    print(response.text)
    
    # Check for failure and append to failures list
    if ((response.status_code != 200) and (response.status_code != 201)):
        failures.append(guid + '\t' + payor_classification['coveredEntityId'] + '\t' + payor_classification['effectiveDate'])
        print(response.text)

# Write failures to a file
with open('local_payor_classification_failures.txt', 'w') as f:
    f.write('''These are the mappings that failed.
-----------------------------------\n
Contract GUID\t\t\t\t\t\t\t\tFee Set GUID
--------------------------------------------------------------------------------
''')
    for failure in failures:
        f.write(failure + '\n')
