resource "aws_security_group_rule" "ingress_rule_ssh" {
#  #count = "${var.create ? length(var.ingress_rules) : 0}"

  security_group_id = "sg-0af15a407cf764fc7"
  type              = "ingress"

  cidr_blocks      = ["0.0.0.0/0"]
  description      = "this security group rule ssh"

  from_port = "22"
  to_port   = "22"
  protocol  = "tcp"
}

resource "aws_security_group_rule" "ingress_rule_http" {
#  #count = "${var.create ? length(var.ingress_rules) : 0}"

  security_group_id = "sg-0af15a407cf764fc7"
  type              = "ingress"

  cidr_blocks      = ["0.0.0.0/0"]
  description      = "this security group rule http"

  from_port = "80"
  to_port   = "80"
  protocol  = "tcp"
}
