[[http_service.checks]]
interval = "5s"
grace_period = "4s"
method = "post"
path = "/health"
protocol = "http"
timeout = "5s"
tls_skip_verify = false


[http_service]
internal_port = 8080
force_https = true
auto_stop_machines = true
auto_start_machines = true
min_machines_running = 0
processes = ["app"]
