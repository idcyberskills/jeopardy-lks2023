<?php
    require 'vendor/autoload.php';
    use Sabre\DAV\Client;

    $settings = array(
        'baseUri' => 'http://davos/restricted/',
        'userName' => 'user',
        'password' => 'bdChWzznlMlVOEBXmIkjiuJJIE9htIav',
        'proxy' => '',
    );
    
    $client = new Client($settings);
    
    $result = $client->propfind('flag.txt', array(
        '{DAV:}displayname',
        '{DAV:}getcontentlength',
        '{DAV:}getlastmodified',
    ));

    echo "Name: " . $result["{DAV:}displayname"] . '<br>';
    echo "Last Modified: " . $result["{DAV:}getlastmodified"] . '<br>';

?>

<!-- http://localhost:8888/public -->