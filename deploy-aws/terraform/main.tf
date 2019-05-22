provider "aws" {
  region                  = "eu-west-1"
  shared_credentials_file = "/home/user/.aws/credentials"
  profile                 = "default"
}

resource "aws_key_pair" "auth" {
  key_name   = "local_user"
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDT3mawBpT2cqQDVUuzkPpeOyx8718G67LRhld7OaNsAFeBhYrnv4WUPv90irRZu5hSHPne6+YkpZA26dt7TjhoybQ0Hf9uls3M+alKOjGv+nhMYr1+zVZLa9wuzPqwzQXXnIExcBvRY5znSzXraYi0klA+DAXQ0yK8O974VNBu2JGr5SDEayNG7SxiUXUVJ9nbluHaj8QLpg3vsVhshkm9++qvvBu1/QwbQFd4sOK29bzrnhMDDGVzVKYSJgwRogoYg6ZOX4Kmw7JTN0yDdroZu49YHAuXhhJr3dmCRxwtdC64l2AYl120E8HD9m/YHfmALwsru2zSk4TMiDE+vP/1 user@VirtualBox"
}

resource "aws_security_group" "this" {
  #count = "${var.create && ! var.use_name_prefix ? 1 : 0}"

  name        = "this"
  description = "this security group"
  vpc_id      = "vpc-e04e7786"

#  tags = "[this]"
}

resource "aws_instance" "runcalc-main-app" {
  ami = "ami-0060225952ea8c9cd"
  instance_type = "t2.nano"
  tags {
    Name = "runcalc-main-app"
  }

  security_groups = [
      "this"
  ]

  key_name = "local_user"

}
