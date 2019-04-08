provider "google" {
  version = "1.4.0"
  project = "${var.project}"
  region  = "${var.region}"
}
resource "google_compute_instance" "app" {
  name          = "runcalc-terraform"
  machine_type  = "f1-micro"
  zone          = "europe-west1-b"
  # определение загрузочного диска
  boot_disk {
    initialize_params {
      image = "${var.app_disk_image}"
    }
  }
  # определение сетевого интерфейса
  network_interface {
    # сеть, к которой присоединить данный интерфейс
    network = "default"
    # использовать ethemeral ip для доступа из интернет
    access_config {}
  }
  metadata {
    ssh-keys = "user:${file(var.public_key_path)}"
  }
  tags = ["runcalc-terraform"]
  connection {
    type  = "ssh"
    user  = "user"
    agent = false
    private_key = "${file("~/.ssh/appuser")}"
  }
#  provisioner "file" {
#    source      = "files/runcalc.service"
#    destination = "/tmp/runcalc.service"
#  }
  provisioner "remote-exec" {
    script = "files/deploy.sh"
  }
}

resource "google_compute_firewall" "firewall_8080" {
  name     = "allow-8080-default"
  # Название сети для которой действует правило
  network  = "default"
  # Какой доступ разрешаем
  allow {
    protocol = "tcp"
    ports    = ["8080"]
  }
  # кому разрешаем ходить 
  source_ranges = ["0.0.0.0/0"]
  # на какой тэг вешается правило
  target_tags = ["runcalc-terraform"]
}

# существует по дефолту в GCP для всех проектов
#resource "google_compute_firewall" "firewall_ssh" {
#  name    = "default-allow-ssh"
#  network = "default"
#  allow {
#    protocol = "tcp"
#    ports    = ["22"]
#  }
#  source_ranges = ["0.0.0.0/0"]
#}
