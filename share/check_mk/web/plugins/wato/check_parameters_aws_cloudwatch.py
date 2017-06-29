register_check_parameters(
    subgroup_virt,
    "aws_cloudwatch",
    _("AWS Cloudwatch levels"),
    Dictionary(
        elements = [
            ("levels",
            Tuple(
                title = "Levels for Cloudwach metrics",
                elements = [
		    Float( title = _("Critical if below"), default_value = -1e38 ),
		    Float( title = _("Warning if below"), default_value = -1e38 ),
		    Float( title = _("Warning if above"), default_value = 1e38 ),
		    Float( title = _("Critical if above"), default_value = 1e38 ),
                ])),
        ]),
    TextAscii(
        title = _("Item Name"),
        help = _("Name of the Service description without the AWS Cloudwatch prefix")
    ),
    "dict"
)
