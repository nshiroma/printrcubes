<?php

$curl = curl_init();
$filename='packed-unit.pdf';
$file_path = '/var/www/html/printix/';
$file_path .=$filename;
$printer_queue = 'QL800_TST';

curl_setopt_array($curl, array(
  CURLOPT_URL => 'http://64.225.102.244:5000/print',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_POST => true,
  CURLOPT_POSTFIELDS => array(
    'pdf' => new CURLFILE($file_path),
    'queue_name' => $printer_queue,
    'filename' => $filename
  ),
));

$response = curl_exec($curl);
//comment
curl_close($curl);
echo $response;
