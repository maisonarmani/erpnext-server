from __future__ import unicode_literals
from frappe import _
from tools_box.controllers.setup import get_support_section, get_extra_support_reports

def get_data():
	return [
		{
			"label": _("Issues"),
			"items": [
				{
					"type": "doctype",
					"name": "Issue",
					"description": _("Support queries from customers."),
				},
				{
					"type": "doctype",
					"name": "Communication",
					"description": _("Communication log."),
				},
			]
		},
		{
			"label": _("Warranty"),
			"items": [
				{
					"type": "doctype",
					"name": "Warranty Claim",
					"description": _("Warranty Claim against Serial No."),
				},
				{
					"type": "doctype",
					"name": "Serial No",
					"description": _("Single unit of an Item."),
				},
			]
		},
		get_support_section(),
		{
			"label": _("Reports"),
			"icon": "fa fa-list",
			"items": [
				{
					"type": "page",
					"name": "support-analytics",
					"label": _("Support Analytics"),
					"icon": "fa fa-bar-chart"
				},
				{
					"type": "report",
					"name": "Minutes to First Response for Issues",
					"doctype": "Issue",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "Support Hours",
					"doctype": "Issue",
					"is_query_report": True
				},
			]
		},
		get_extra_support_reports()
	]
