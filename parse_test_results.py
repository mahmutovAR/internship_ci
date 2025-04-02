import xml.etree.ElementTree as ET
from os import environ


tree = ET.parse('test_results')
root = tree.getroot()

testsuite = root.find('testsuite')
failed = testsuite.get('failures')
skipped = testsuite.get('skipped')
total = testsuite.get('tests')
passed = int(total) - int(skipped) - int(failed)

environ['TEST_RESULT_TOTAL'] = total
environ['TEST_RESULT_PASSED'] = str(passed)
environ['TEST_RESULT_SKIPPED'] = skipped
environ['TEST_RESULT_FAILED'] = failed
