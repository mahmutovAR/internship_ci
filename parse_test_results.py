import xml.etree.ElementTree as ET


tree = ET.parse('pytest_results')
root = tree.getroot()

testsuite = root.find('testsuite')
failed = testsuite.get('failures')
skipped = testsuite.get('skipped')
total = testsuite.get('tests')
passed = int(total) - int(skipped) - int(failed)

output_data = f"""
<p>
TOTAL_TESTS = {total}<br>
PASSED_TESTS = {passed}<br>
SKIPPED_TESTS = {skipped}<br>
FAILED_TESTS = {failed}
</p>
"""

with open('pytest_output.html', 'w') as file_to_write:
    file_to_write.write(output_data)
