var formPrefix = '/remindr/senior/';
var apptSuffix = '/appointment/add/';
var medsSuffix = '/medication/add/';

function showProfilePanel(e, id) {
	e.preventDefault();
	var srcLi = $(e.srcElement).parent();
	var panel = $('#profileContent').find(id);
	if (!srcLi.hasClass('active')) {
		srcLi.parent().find('li.active').removeClass('active');
		srcLi.addClass('active');
		panel.parent().find('.profilePanel.active').removeClass('active');
		panel.addClass('active');

	}
};

function formActionCorrection(seniorId) {
	var apptUrl = formPrefix.concat(seniorId).concat(apptSuffix);
	var medsUrl = formPrefix.concat(seniorId).concat(medsSuffix);
	$('#apptForm form').attr('action', apptUrl);
	$('#medsForm form').attr('action', medsUrl);
}

function populateProfile(contactListItem) {
	var contactInfo = $(contactListItem).find('.contactName');
	var contactNumber = contactInfo.attr('id');
	var contactName = contactInfo.find('h3').html();

	var contactBanner = $('#profileHeader');
	$('#profileHeader').find('.contactName h3').html(contactName);
	$('#profileHeader').find('.contactName h5').html(contactNumber);
}

function populateAppointments(jsonArray) {
	clearAppointments();
	var appointmentList = $('#profileAppt #scheduleList .listGroup');
	for(i = 0; i < jsonArray.length; i++) {
		var templateBlock = $($('template#listItem').html());
		templateBlock.find('.itemDetail').html(jsonArray[i].fields.appointment);
		templateBlock.find('.itemDelete').html("<a href=\"/remindr/reminder/" + jsonArray[i].pk + "/delete\">Delete</a>")
		var date = dateToString(jsonArray[i].fields.time_to_take);
		templateBlock.find('.itemTime').html(date);
		appointmentList.append(templateBlock);

	}
}

function populateMedication(jsonArray) {
	clearMedication();
	var medicationList = $('#profileMeds #scheduleList .listGroup');
	for (i = 0; i < jsonArray.length; i++) {
		var templateBlock = $($('template#listItem').html());
		templateBlock.find('.itemDetail').html(jsonArray[i].fields.name);
		templateBlock.find('.itemTime').html(jsonArray[i].fields.dosage_amount + " " +jsonArray[i].fields.dosage_unit);
		medicationList.append(templateBlock);
	}	
}

function clearAppointments() {
	var appointmentList = $('#profileAppt #scheduleList .listGroup');
	appointmentList.empty();
}

function clearMedication() {
	var medicationList = $('#profileMeds #scheduleList .listGroup');
	medicationList.empty();
}

function dateToString(dateStr) {
	var months = [ "Jan.", "Feb.", "Mar.", "Apr.", "May", "Jun.", 
               "Jul.", "Aug.", "Sept.", "Oct.", "Nov.", "Dec." ];

	var halves = dateStr.split("T");
	var time = halves[1].slice(0,5);
	var dateParts = halves[0].split("-");

	var month = months[parseInt(dateParts[1]) - 1];

	return month+" "+dateParts[2]+" "+dateParts[0]+" "+time;
}


$(document).ready(function(){
	$('li.contactListItem:not(:last-child)').on('click', function(e){
		e.preventDefault();
		var senior_id = e.currentTarget.id;
		populateApptAjax(senior_id);
		populateMedAjax(senior_id);
		populateProfile(e.currentTarget);
		formActionCorrection(senior_id);
	});

	$('#id_recurring').on('change', function() {
		if(this.checked) {
			$('#repeat legend').html('Repeat Behaviour');
			$('li#start label, li#end, li#frequency').show();
			$('li#start label').attr('style', 'display: block;');
		} else {
			$('li#start label, li#end, li#frequency').hide();
			$('#repeat legend').html('Date');
		}
	});

	$('#id_phone_number').on('change', function(){
		var re = new RegExp("^\\d{10}$");
		if (!re.test(this.value)) {
			$(this.parentElement).addClass('danger');
			$('#seniorSubmitBtn').addClass('disable');
		} else {
			$(this.parentElement).removeClass('danger');
			$('#seniorSubmitBtn').removeClass('disable');
		}
		// if (!this.value.match(\d{3}-\d{3}-\d{4}|\d{10})) {
		// 	debugger;
		// }
	})
});