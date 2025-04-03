import xml.etree.ElementTree as ET


tree = ET.parse('test_results')
root = tree.getroot()

testsuite = root.find('testsuite')
failed = testsuite.get('failures')
skipped = testsuite.get('skipped')
total = testsuite.get('tests')
timestamp = testsuite.get('timestamp')
passed = int(total) - int(skipped) - int(failed)
print(f'path = {__file__}, timestamp = {timestamp}')

output_data = f"TOTAL_TESTS={total}\nPASSED_TESTS={passed}\nSKIPPED_TESTS={skipped}\nFAILED_TESTS={failed}"

with open('tests_output.txt', 'w') as file_to_write:
    file_to_write.write(output_data)
