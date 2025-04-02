import xml.etree.ElementTree as ET


tree = ET.parse('test_results')
root = tree.getroot()

testsuite = root.find('testsuite')
failed = testsuite.get('failures')
skipped = testsuite.get('skipped')
total = testsuite.get('tests')
passed = int(total) - int(skipped) - int(failed)

output_data = f"""Tests: {total}\n
Passed: {passed}\n
Skipped: {skipped}\n
Failed: {failed}"""

with open('tests_output.txt', 'w') as file_to_write:
    file_to_write.write(output_data)
