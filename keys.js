var next = function() { window.location = $('#right').attr("href"); };
var prev = function() { window.location = $('#left').attr("href"); };
Mousetrap.bind('space', next);
Mousetrap.bind('right', next);
Mousetrap.bind('left', prev);
