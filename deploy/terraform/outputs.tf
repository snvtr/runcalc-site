output "main-app_external_ip" {
  value = "${google_compute_instance.main-app.network_interface.0.access_config.0.assigned_nat_ip}"
}

output "json-app_external_ip" {
  value = "${google_compute_instance.json-app.network_interface.0.access_config.0.assigned_nat_ip}"
}
