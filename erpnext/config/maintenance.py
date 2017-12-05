from frappe import _

from tools_box.controllers.setup import get_maintenance_section, get_extra_maintenance_reports

def get_data():
	return [
		{
			"label": _("Maintenance"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Maintenance Schedule",
					"description": _("Plan for maintenance visits."),
				},
				{
					"type": "doctype",
					"name": "Maintenance Visit",
					"description": _("Visit report for maintenance call."),
				},
				{
					"type": "report",
					"name": "Maintenance Schedules",
					"is_query_report": True,
					"doctype": "Maintenance Schedule"
				},
				{
					"type": "doctype",
					"name": "Warranty Claim",
					"description": _("Warranty Claim against Serial No."),
				},
			]
		},
		get_maintenance_section(),
		get_extra_maintenance_reports()
	]