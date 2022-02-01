#!/bin/bash
echo -e 'Script for startign api tests and generating report\n'
if [ -f result.txt ]
then
  echo -e 'Deleting previous results...\n'
  sleep 2
  echo -e 'The previos results has been deleted!!!\n'
  sleep 2
else
  echo -e 'There is no result.txt, this file will be created...\n'
  sleep 2
fi
pytest -v --alluredir=results/ tests_api | tee result.txt
echo 'Generating allure report...'
sleep 3
allure serve results/

