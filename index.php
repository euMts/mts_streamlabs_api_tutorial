<?php

$query = http_build_query([
    "response_type" => "code",
    "client_id" => "SEU_CLIENT_ID",
    "redirect_uri" => "http://localhost:8080/auth",
    "scope" => "donations.create donations.read alerts.create legacy.token socket.token points.read points.write alerts.write credits.write profiles.write jar.write wheel.write mediashare.control"
]);

header("Location: https://streamlabs.com/api/v1.0/authorize?$query");
exit;