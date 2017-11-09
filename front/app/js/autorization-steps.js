$(document).ready(function() { // Ждём загрузки страницы
	var steps = $("form").children(".step"); // находим все шаги формы
	$(steps[0]).show(); // показываем первый шаг
	var current_step = 0; // задаем текущий шаг
    $("a.authorization__prev-step").hide();
	$("a.authorization__next-step").click(function(){	// Событие клика на ссылку "Следующий шаг"
			if (current_step == steps.length-2) { // проверяем, будет ли следующий шаг последним
				$(this).hide(); // скрываем ссылку "Следующий шаг"
				$("form input[type=button]").show(); // показываем кнопку "Регистрация"
			}
			$(".authorization__steps-links").css("justify-content", "space-between");
			$("a.authorization__prev-step").show(); // показываем ссылку "Назад"
			current_step++; // увеличиваем счетчик текущего слайда
			changeStep(current_step); // меняем шаг
	});
	
	$("a.authorization__prev-step").click(function(){	// Событие клика на маленькое изображение
		if (current_step == 1) { // проверяем, будет ли предыдущий шаг первым
			$(this).hide(); // скрываем ссылку "Назад"
			$(".authorization__steps-links").css("justify-content", "flex-end");
		}
		$("form input[type=button]").hide(); // скрываем кнопку "Регистрация"
		$("a.authorization__next-step").show(); // показываем ссылку "Следующий шаг"
		current_step--; // уменьшаем счетчик текущего слайда
		changeStep(current_step);// меняем шаг
	});
	
	function changeStep(i) { // функция смены шага
		$(steps).hide(); // скрываем все шаги
		$(steps[i]).show(); // показываем текущий
	}
});