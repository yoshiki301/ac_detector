<?php
require "vendor/autoload.php";
use Abraham\TwitterOAuth\TwitterOAuth;

$consumerKey       = "";
$consumerSecret    = "";
$accessToken       = "";
$accessTokenSecret = "";

$twitter = new TwitterOAuth($consumerKey, $consumerSecret, $accessToken, $accessTokenSecret);
$result = $twitter->post("statuses/update", array("status" => "twitterOAuthからツイート"));

