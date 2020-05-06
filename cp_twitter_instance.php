<?php
require "vendor/autoload.php";
use Abraham\TwitterOAuth\TwitterOAuth;

$consumerKey       = "hzTH5JMYenuZsPdrqGzK9bToK";
$consumerSecret    = "Ef8Mh6V3hQKoIgWQex9DKr5S7PBhUJddT9lZvENQ7GfMKcOmNI";
$accessToken       = "3303913819-jrH0Ob7PSdZL2lhDUFQSgSY2WslC1k1NWswC4JL";
$accessTokenSecret = "jkFsU19wKEMp9B3ld9AVqoLqEiW1XRwTQkySuSeVi2WrK";

$twitter = new TwitterOAuth($consumerKey, $consumerSecret, $accessToken, $accessTokenSecret);
$result = $twitter->post("statuses/update", array("status" => "twitterOAuthからツイート"));

