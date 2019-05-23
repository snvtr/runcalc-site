resource "aws_security_group_rule" "ingress_rule_ssh" {

  security_group_id = "${aws_security_group.this.id}"
  type              = "ingress"

  cidr_blocks      = ["0.0.0.0/0"]
  description      = "this security group rule ssh"

  from_port = "22"
  to_port   = "22"
  protocol  = "tcp"
}

resource "aws_security_group_rule" "ingress_rule_http" {

  security_group_id = "${aws_security_group.this.id}"
  type              = "ingress"

  cidr_blocks      = ["0.0.0.0/0"]
  description      = "this security group rule http"

  from_port = "80"
  to_port   = "80"
  protocol  = "tcp"
}

resource "aws_security_group_rule" "ingress_rule_http_8080" {

  security_group_id = "${aws_security_group.this.id}"
  type              = "ingress"

  cidr_blocks      = ["0.0.0.0/0"]
  description      = "this security group rule http 8080"

  from_port = "8080"
  to_port   = "8080"
  protocol  = "tcp"
}

resource "aws_security_group_rule" "egress_rule_all" {

  security_group_id = "${aws_security_group.this.id}"
  type              = "egress"

  cidr_blocks      = ["0.0.0.0/0"]
  description      = "this security group allow all tcp traffic out"

  from_port = "0"
  to_port   = "65535"
  protocol  = "tcp"
}
