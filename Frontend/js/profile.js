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