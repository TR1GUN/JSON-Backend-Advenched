function get_settings(uri, parser) {
    var request = new XMLHttpRequest();
    request.open('GET', uri);
	request.setRequestHeader('X-Protocol-USPD', '40');
    request.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200) {
                var response = JSON.parse(this.responseText);
                parser(response);
            }
			if (this.status == 403)
			{
				redirect_to_home_page();
			}
        }
    }
    request.send(null);
}

function set_settings(uri, settings, method) {
	var request = new XMLHttpRequest();
	request.open(method, uri);
	request.setRequestHeader('X-Protocol-USPD', '40');
	request.setRequestHeader("Content-type", "application/json");
	request.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200) {
				window.location.reload();
            }
			if (this.status == 403)
			{
				redirect_to_home_page();
			}
        }
    }
	request.send(JSON.stringify(settings));
};

function del_settings(uri) {
	var request = new XMLHttpRequest();
	request.open('DELETE', uri);
	request.setRequestHeader('X-Protocol-USPD', '40');
	request.setRequestHeader("Content-type", "application/json");
	request.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200) {
            }
			if (this.status == 403)
			{
				redirect_to_home_page();
			}
        }
    }
	request.send(null);
};

function redirect_to_home_page() {
	document.location.href = '/';
}

function add_input(row, id)
{
	var td = document.createElement("TD");
	td.setAttribute("id", id);
	var input = document.createElement("input")	;
	td.appendChild(input);
	row.appendChild(td);
}

function add_checkbox(row, id)
{
	var td = document.createElement("TD");
	td.setAttribute("id", id);
	var input = document.createElement("input");
	input.setAttribute("type","checkbox");
	td.appendChild(input);
	row.appendChild(td);
}

function add_textarea(row, id, rows, cols)
{
	var td = document.createElement("TD");
	td.setAttribute("id", id);
	var input = document.createElement("textarea");
	input.rows = rows;
	input.cols = cols;
	td.appendChild(input);
	row.appendChild(td);
}

function add_select(row, id, params)
{
	var td = document.createElement("TD");
	td.setAttribute("id", id);
	var select = document.createElement("select");
	var i;
	for (i = 0; i < params.length; ++i) {
		option = document.createElement('option');
		option.innerText = params[i];
		option.setAttribute("value", i);
		select.appendChild(option);
	}
	td.appendChild(select);
	row.appendChild(td);
}

function add_custom_select(row, id, params)
{
	var td = document.createElement("TD");
	td.setAttribute("id", id);
	var select = document.createElement("select");
	var i;
	for (i = 0; i < params.length; ++i) {
		option = document.createElement('option');
		option.innerText = (params[i])[0];
		option.setAttribute("value", params[i][1]);
		select.appendChild(option);
	}
	td.appendChild(select);
	row.appendChild(td);
}

function add_meter_action_row()
{
	var tbody = document.getElementById('Settings');
	var row = document.createElement("TR")
	add_input(row,"id");
	add_input(row,"archTypesName");
	add_input(row,"metersName");
	tbody.appendChild(row);	
}

function add_meter_row()
{
	var tbody = document.getElementById('Meters');
	var row = document.createElement("TR")
	add_input(row,"id");
	add_input(row,"pId");
	add_custom_select(row,"type",[["Меркурий200","Mercury200"],["Меркурий203","Mercury203"],["Меркурий206","Mercury206"],["Меркурий23x","Mercury23x"],["Меркурий СПОДЭС","SPODES_M2XX"],["Энергомера СПОДЭС","SPODES_CE"],["Милур СПОДЭС","SPODES_MILUR"],["СЕ102","SE102"],["СЕ102М","SE102M"],["СЕ301","SE301"],["СЕ303","SE303"],["СЭБ2А","SEB2a"],["СЭТ4ТМ","SETxTM"],["ПСЧхТМ","PSCHxTM"],["Альфа1140","A1140"],["ТОПАЗ","TOPAZ"],["НЕВА1xx","NEVA1xx"],["НЕВА3xx","NEVA3xx"],["МИЛУР IC","MILUR IC"],["Милур10x","MILUR10x"],["Милур30x","MILUR30x"],["СОЭ55/215","SOE55_215"],["СОЭ55/217","SOE55_217"],["СОЭ55/415","SOE55_415"],["СТЭ561","STE561"],["ИНТЕГРА10х","INTEGRA10x"],["УМТВ10","UMTV10"],["Пульсар","Pulsar"],["ST410","ST410"]]);
	add_input(row,"addr");
	add_input(row,"passRd");
	add_input(row,"passWr");	
	add_custom_select(row,"iface",[["Интерфейс 1","Iface1"],["Интерфейс 2","Iface2"],["Интерфейс 3","Iface3"],["Интерфейс 4","Iface4"],["Ethernet","Ethernet"],["Интерфейс концентратора","Hub"]]);
	add_input(row,"ifaceCfg");	
	add_input(row,"rtuObjType");
	add_input(row,"rtuObjNum");
	add_input(row,"rtuFider");
	tbody.appendChild(row);	
}

function add_charge_station_row()
{
	var tbody = document.getElementById('ChargeStations');
	var row = document.createElement("TR")
	add_input(row,"id");
	add_custom_select(row,"type",[["ЗСЭ-500Т, НПП Энергия","ZSE-500T"]]);	
	add_input(row,"addr");
	add_input(row,"port");
	add_input(row,"mqttId");	
	tbody.appendChild(row);	
}

function add_uart_settings_row()
{
	var tbody = document.getElementById('Settings');
	var row = document.createElement("TR")
	add_input(row,"id");
	add_custom_select(row,"iface",[["Интерфейс 1",0],["Интерфейс 2",1],["Интерфейс 3",2],["Интерфейс 4",3],["Интерфейс 5",4], ["Интерфейс модема",5]]);
	add_custom_select(row,"br",[["Автоматически",0],["300",300],["600",600],["1200",1200],["2400",2400],["4800",4800],["9600",9600],["19200",19200],["38400",38400],["57600",57600],["115200",115200]]);	
	add_custom_select(row,"size",[["7",7],["8",8]]);	
	add_select(row,"parity",["Отсутствует","Контроль четности","Контроль нечетности"]);	
	add_custom_select(row,"stop",[["1",1],["2",2]]);	
	add_select(row,"line",["Автоматически","Линия питания 1","Линия питания 2","Линия питания 3","Линия питания 4","Линия питания 5"]);	
	tbody.appendChild(row);	
}

function add_schdl_event_row()
{
	var tbody = document.getElementById('Settings');
	var row = document.createElement("TR");
	add_input(row,"id");
	add_input(row,"month");		
	add_input(row,"day");
	add_input(row,"hour");
	add_input(row,"min");
	tbody.appendChild(row);	
}

function add_sntp_srv_row()
{
	var tbody = document.getElementById('Settings');
	var row = document.createElement("TR");
	add_input(row,"addr");
	tbody.appendChild(row);	
}

function add_sntp_action_row()
{
	var tbody = document.getElementById('Settings');
	var row = document.createElement("TR")
	add_input(row,"id");
	add_select(row,"eventType",["Расписание","Изменение дискретного входа"]);
	add_input(row,"eventId");	
	tbody.appendChild(row);	
}

function add_event_manager_row()
{
	var tbody = document.getElementById('Settings');
	var row = document.createElement("TR")
	add_input(row,"id");
	add_custom_select(row,"eventType",[["Расписание","Scheduler"]]);	
	add_input(row,"eventId");
	add_custom_select(row,"actionType",[["Опрос ПУ","Poller"]]);	
	add_input(row,"actionId");
	tbody.appendChild(row);	
}

function add_meter_template_row()
{
	var tbody = document.getElementById('Settings');
	var row = document.createElement("TR")
	add_input(row,"name");
	tbody.appendChild(row);	
}

function add_meter_template_settings_row()
{
	var tbody = document.getElementById('Settings');
	var row = document.createElement("TR")
	add_input(row,"meterId");
	tbody.appendChild(row);	
}

function add_meter_arch_template_row()
{
	var tbody = document.getElementById('Settings');
	var row = document.createElement("TR")
	add_input(row,"name");
	tbody.appendChild(row);	
}

function add_meter_arch_template_settings_row()
{
	var tbody = document.getElementById('Settings');
	var row = document.createElement("TR")
	add_custom_select(row,"ArchType",[["конфигурация электросчетчика","ElConfig"],["конфигурация модуля дискретных вводов/выводов","DigConfig"],["конфигурация концентратора импульсных счетчиков","PlsConfig"],["мгновенные показания энергии электросчетчика","ElMomentEnergy"],["текущие ПКЭ электросчетчика","ElMomentQuality"],["показания электросчетчика на начало суток","ElDayEnergy"],["потребление электросчетчика за сутки","ElDayConsEnergy"],["показания электросчетчика на начало месяца","ElMonthEnergy"],["потребление электросчетчика за месяц","ElMonthConsEnergy"],["профили мощности первого массива профилей мощности электросчетчика","ElArr1ConsPower"],["мгновенные показания модуля дискретных вводов/выводов","DigMomentState"],["архив изменения состояний модуля дискретных вводов/выводов","DigJournalState"],["мгновенные показания энергии концентратора импульсных счетчиков","PlsMomentPulse"],["показания концентратора импульсных счетчиков на начало суток","PlsDayPulse"],["показания концентратора импульсных счетчиков на начало месяца","PlsMonthPulse"],["показания на начало часа концентратора импульсных счетчиков","PlsHourPulse"],["журнал управление питанием электросчетчика","ElJrnlPwr"],["журнал коррекция времени электросчетчика","ElJrnlTimeCorr"],["журнал коррекция времени концентратора импульсных счетчиков","PlsJrnlTimeCorr"],["журнал сброс показаний электросчетчика","ElJrnlReset"],["журнал инициализация первого массива профилей электросчетчика","ElJrnlC1Init"],["журнал инициализация второго массива профилей электросчетчика","ElJrnlC2Init"],["журнал коррекция тарификатора электросчетчика","ElJrnlTrfCorr"],["журнал открытие крышки электросчетчика","ElJrnlOpen"],["журнал неавторизованный доступ электросчетчика","ElJrnlUnAyth"],["журнал управление фазой А электросчетчика","ElJrnlPwrA"],["журнал управление фазой В электросчетчика","ElJrnlPwrB"],["журнал управление фазой C электросчетчика","ElJrnlPwrC"],["журнал программирование электросчетчика","ElJrnlProg"],["журнал управление реле электросчетчика","ElJrnlRelay"],["журнал лимит суммарной энергии электросчетчика","ElJrnlLimESumm"],["журнал потарифный лимит энергии электросчетчика","ElJrnlLimETrf"],["журнал лимит энергии тарифа 1 электросчетчика","ElJrnlLimETrf1"],["журнал лимит энергии тарифа 2 электросчетчика","ElJrnlLimETrf2"],["журнал лимит энергии тарифа 3 электросчетчика","ElJrnlLimETrf3"],["журнал лимит энергии тарифа 4 электросчетчика","ElJrnlLimETrf4"],["журнал ограничение максимального напряжения фазы А электросчетчика","ElJrnlLimUAMax"],["журнал ограничение минимального напряжения фазы А электросчетчика","ElJrnlLimUAMin"],["журнал ограничение максимального напряжения фазы В электросчетчика","ElJrnlLimUBMax"],["журнал ограничение минимального напряжения фазы В электросчетчика","ElJrnlLimUBMin"],["журнал ограничение максимального напряжения фазы С электросчетчика","ElJrnlLimUCMax"],["журнал ограничение минимального напряжения фазы С электросчетчика","ElJrnlLimUCMin"],["журнал ограничение максимального расхождения напряжения фаз А и В электросчетчика","ElJrnlLimUABMax"],["журнал ограничение минимального расхождения напряжения фаз А и В электросчетчика","ElJrnlLimUABMin"],["журнал ограничение максимального расхождения напряжения фаз В и С электросчетчика","ElJrnlLimUBCMax"],["журнал ограничение минимального расхождения напряжения фаз В и С электросчетчика","ElJrnlLimUBCMin"],["журнал ограничение максимального расхождения напряжения фаз С и А электросчетчика","ElJrnlLimUCAMax"],["журнал ограничение минимального расхождения напряжения фаз С и А электросчетчика","ElJrnlLimUCAMin"],["журнал ограничение максимального тока фазы А электросчетчика","ElJrnlLimIAMax"],["журнал ограничение максимального тока фазы В электросчетчика","ElJrnlLimIBMax"],["журнал ограничение максимального тока фазы С электросчетчика","ElJrnlLimICMax"],["журнал ограничение максимальной частоты сети электросчетчика","ElJrnlLimFreqMax"],["журнал ограничение минимальной частоты сети электросчетчика","ElJrnlLimFreqMin"],["журнал ограничение мощности электросчетчика","ElJrnlLimPwr"],["журнал ограничение прямой активной мощности электросчетчика","ElJrnlLimPwrPP"],["журнал ограничение прямой реактивной мощности электросчетчика","ElJrnlLimPwrPM"],["журнал ограничение обратной активной мощности электросчетчика","ElJrnlLimPwrQP"],["журнал ограничение обратной реактивной мощности электросчетчика","ElJrnlLimPwrQM"],["журнал реверс электросчетчика","ElJrnlRvr"]]);
	tbody.appendChild(row);	
}

function add_json_auth_settings_row()
{
	var tbody = document.getElementById('Settings');
	var row = document.createElement("TR")
	add_input(row,"id");
	add_input(row,"login");
	add_input(row,"password");
	add_select(row,"lvl",["Нет доступа","Пользователь","Администратор"]);
	tbody.appendChild(row);	
}

function add_meter_data_eng_row()
{
	var tbody = document.getElementById('MeterData');
	var row = document.createElement("TR")
	add_input(row,"id");
	add_input(row,"serial");
	add_input(row,"time");
	add_input(row,"timediff");
	add_input(row,"Ap0");
	add_input(row,"Ap1");
	add_input(row,"Ap2");
	add_input(row,"Ap3");
	add_input(row,"Ap4");
	add_input(row,"Am0");
	add_input(row,"Am1");
	add_input(row,"Am2");
	add_input(row,"Am3");
	add_input(row,"Am4");
	add_input(row,"Rp0");
	add_input(row,"Rp1");
	add_input(row,"Rp2");
	add_input(row,"Rp3");
	add_input(row,"Rp4");
	add_input(row,"Rm0");
	add_input(row,"Rm1");
	add_input(row,"Rm2");
	add_input(row,"Rm3");
	add_input(row,"Rm4");
	tbody.appendChild(row);	
}

function add_meter_data_din_row()
{
	var tbody = document.getElementById('MeterData');
	var row = document.createElement("TR")
	add_input(row,"id");
	add_input(row,"serial");
	add_input(row,"time");
	add_input(row,"timediff");
	add_checkbox(row,"Chnl1");
	add_checkbox(row,"Chnl2");
	add_checkbox(row,"Chnl3");
	add_checkbox(row,"Chnl4");
	add_checkbox(row,"Chnl5");
	add_checkbox(row,"Chnl6");
	add_checkbox(row,"Chnl7");
	add_checkbox(row,"Chnl8");
	add_checkbox(row,"Chnl9");
	add_checkbox(row,"Chnl10");
	add_checkbox(row,"Chnl11");
	add_checkbox(row,"Chnl12");
	add_checkbox(row,"Chnl13");
	add_checkbox(row,"Chnl14");
	add_checkbox(row,"Chnl15");
	add_checkbox(row,"Chnl16");
	add_checkbox(row,"Chnl17");
	add_checkbox(row,"Chnl18");
	add_checkbox(row,"Chnl19");
	add_checkbox(row,"Chnl20");
	add_checkbox(row,"Chnl21");
	add_checkbox(row,"Chnl22");
	add_checkbox(row,"Chnl23");
	add_checkbox(row,"Chnl24");
	add_checkbox(row,"Chnl25");
	add_checkbox(row,"Chnl26");
	add_checkbox(row,"Chnl27");
	add_checkbox(row,"Chnl28");
	add_checkbox(row,"Chnl29");
	add_checkbox(row,"Chnl30");
	add_checkbox(row,"Chnl31");
	add_checkbox(row,"Chnl32");
	tbody.appendChild(row);	
}

function add_meter_data_qual_row()
{
	var tbody = document.getElementById('MeterData');
	var row = document.createElement("TR")
	add_input(row,"id");
	add_input(row,"serial");
	add_input(row,"time");
	add_input(row,"timediff");
	add_input(row,"UA");
	add_input(row,"UB");
	add_input(row,"UC");
	add_input(row,"IA");
	add_input(row,"IB");
	add_input(row,"IC");
	add_input(row,"PS");
	add_input(row,"PA");
	add_input(row,"PB");
	add_input(row,"PC");
	add_input(row,"QS");
	add_input(row,"QA");
	add_input(row,"QB");
	add_input(row,"QC");
	add_input(row,"SS");
	add_input(row,"SA");
	add_input(row,"SB");
	add_input(row,"SC");
	add_input(row,"AngAB");
	add_input(row,"AngBC");
	add_input(row,"AngAC");
	add_input(row,"kPS");
	add_input(row,"kPA");
	add_input(row,"kPB");
	add_input(row,"kPC");
	add_input(row,"Freq");
	tbody.appendChild(row);	
}

function add_meter_data_config_row()
{
	var tbody = document.getElementById('MeterData');
	var row = document.createElement("TR")
	add_input(row,"id");
	add_input(row,"serial");
	add_input(row,"time");
	add_input(row,"timediff");
	add_input(row,"kU");
	add_input(row,"kI");
	add_input(row,"Const");
	add_checkbox(row,"isClock");
	add_checkbox(row,"isTrf");
	add_checkbox(row,"isDst");
	add_checkbox(row,"isRp");
	add_checkbox(row,"isAm");
	add_checkbox(row,"isRm");
	add_checkbox(row,"isCons");
	add_input(row,"cTime");
	tbody.appendChild(row);	
}

function add_meter_data_cons_row()
{
	var tbody = document.getElementById('MeterData');
	var row = document.createElement("TR")
	add_input(row,"id");
	add_input(row,"serial");
	add_input(row,"time");
	add_input(row,"timediff");
	add_input(row,"Pp");
	add_input(row,"Pm");
	add_input(row,"Qp");
	add_input(row,"Qm");
	add_checkbox(row,"isMeas");
	add_checkbox(row,"isSummer");
	add_checkbox(row,"isOvfl");
	add_checkbox(row,"isPart");
	tbody.appendChild(row);	
}

function add_meter_data_time_row()
{
	var tbody = document.getElementById('MeterData');
	var row = document.createElement("TR")
	add_input(row,"id");
	add_input(row,"serial");
	add_input(row,"time");
	add_input(row,"timediff");
	tbody.appendChild(row);	
}

function add_meter_data_relay_row()
{
	var tbody = document.getElementById('MeterData');
	var row = document.createElement("TR")
	add_input(row,"id");
	add_input(row,"serial");
	add_input(row,"time");
	add_input(row,"timediff");
	add_input(row,"rId");
	add_input(row,"state");
	tbody.appendChild(row);	
}

function add_meter_data_journal_row()
{
	var tbody = document.getElementById('MeterData');
	var row = document.createElement("TR")
	add_input(row,"id");
	add_input(row,"serial");	
	add_custom_select(row,"type",[["журнал управление питанием электросчетчика","ElJrnlPwr"],["журнал коррекция времени электросчетчика","ElJrnlTimeCorr"],["журнал коррекция времени концентратора импульсных счетчиков","PlsJrnlTimeCorr"],["журнал сброс показаний электросчетчика","ElJrnlReset"],["журнал инициализация первого массива профилей электросчетчика","ElJrnlC1Init"],["журнал инициализация второго массива профилей электросчетчика","ElJrnlC2Init"],["журнал коррекция тарификатора электросчетчика","ElJrnlTrfCorr"],["журнал открытие крышки электросчетчика","ElJrnlOpen"],["журнал неавторизованный доступ электросчетчика","ElJrnlUnAyth"],["журнал управление фазой А электросчетчика","ElJrnlPwrA"],["журнал управление фазой B электросчетчика","ElJrnlPwrB"],["журнал управление фазой C электросчетчика","ElJrnlPwrC"],["журнал программирование электросчетчика","ElJrnlProg"],["журнал управление реле электросчетчика","ElJrnlRelay"],["журнал лимит суммарной энергии электросчетчика","ElJrnlLimESumm"],["журнал потарифный лимит энергии электросчетчика","ElJrnlLimETrf"],["журнал лимит энергии тарифа 1 электросчетчика","ElJrnlLimETrf1"],["журнал лимит энергии тарифа 2 электросчетчика","ElJrnlLimETrf2"],["журнал лимит энергии тарифа 3 электросчетчика","ElJrnlLimETrf3"],["журнал лимит энергии тарифа 4 электросчетчика","ElJrnlLimETrf4"],["журнал ограничение максимального напряжения фазы А электросчетчика","ElJrnlLimUAMax"],["журнал ограничение минимального напряжения фазы А электросчетчика","ElJrnlLimUAMin"],["журнал ограничение максимального напряжения фазы В электросчетчика","ElJrnlLimUBMax"],["журнал ограничение минимального напряжения фазы В электросчетчика","ElJrnlLimUBMin"],["журнал ограничение максимального напряжения фазы С электросчетчика","ElJrnlLimUCMax"],["журнал ограничение минимального напряжения фазы С электросчетчика","ElJrnlLimUCMin"],["журнал ограничение максимального расхождения напряжения фаз А и В электросчетчика","ElJrnlLimUABMax"],["журнал ограничение минимального расхождения напряжения фаз А и В электросчетчика","ElJrnlLimUABMin"],["журнал ограничение максимального расхождения напряжения фаз В и С электросчетчика","ElJrnlLimUBCMax"],["журнал ограничение максимального расхождения напряжения фаз В и С электросчетчика","ElJrnlLimUBCMin"],["журнал ограничение максимального расхождения напряжения фаз С и А электросчетчика","ElJrnlLimUCAMax"],["журнал ограничение минимального расхождения напряжения фаз С и А электросчетчика","ElJrnlLimUCAMin"],["журнал ограничение максимального тока фазы А электросчетчика","ElJrnlLimIAMax"],["журнал ограничение максимального тока фазы В электросчетчика","ElJrnlLimIBMax"],["журнал ограничение максимального тока фазы С электросчетчика","ElJrnlLimICMax"],["журнал ограничение максимальной частоты сети электросчетчика","ElJrnlLimFreqMax"],["журнал ограничение минимальной частоты сети электросчетчика","ElJrnlLimFreqMin"],["журнал ограничение мощности электросчетчика","ElJrnlLimPwr"],["журнал ограничение прямой активной мощности электросчетчика","ElJrnlLimPwrPP"],["журнал ограничение прямой реактивной мощности электросчетчика","ElJrnlLimPwrPM"],["журнал ограничение обратной активной мощности электросчетчика","ElJrnlLimPwrQP"],["журнал ограничение обратной реактивной мощности электросчетчика","ElJrnlLimPwrQM"],["журнал реверс электросчетчика","ElJrnlRvr"]]);
	add_input(row,"time");
	add_input(row,"timediff");
	add_input(row,"eId");
	add_input(row,"etype");
	tbody.appendChild(row);	
}

function add_dout_settings_row()
{
	var tbody = document.getElementById('Settings');
	var row = document.createElement("TR")
        add_custom_select(row,"addr",[["Интерфейс 1","/dev/ttyUSB3"],["Интерфейс 2","/dev/ttyUSB2"],["Интерфейс 3","/dev/ttyUSB1"],["Интерфейс 4","/dev/ttyUSB0"]]);
        add_custom_select(row,"state",[["Автоматически","toggle"],["Включено","on"],["Выключено","off"]]);
	tbody.appendChild(row);	
}

function add_dout_state_row()
{
	var tbody = document.getElementById('State');
	var row = document.createElement("TR")
	add_select(row,"addr",["PWR1","PWR2","PWR3","PWR4","PWR5"]);
	add_select(row,"state",["Выключено","Включено"]);
	tbody.appendChild(row);	
}

function add_dout_set_state_row()
{
	var tbody = document.getElementById('DOutSetState');
	var row = document.createElement("TR")
	add_select(row,"addr",["PWR1","PWR2","PWR3","PWR4","PWR5"]);
	add_select(row,"state",["Вкл","Выкл"]);
	tbody.appendChild(row);	
}

function add_mqtt_srv_row()
{
	var tbody = document.getElementById('Settings');
	var row = document.createElement("TR")
	add_input(row,"id");
	add_input(row,"addr");
	add_input(row,"port");
	add_input(row,"login");
	add_input(row,"password");
	add_input(row,"prefix");
	add_input(row,"deviceID");
	add_select(row,"cropt",["По умолчанию","Без шифрования","Шифрование соединения","STARTTSL"]);
	tbody.appendChild(row);	
}

function add_http_srv_row()
{
	var tbody = document.getElementById('Settings');
	var row = document.createElement("TR")	
        add_custom_select(row,"type",[["Сервер RTU327","rtu327"],["Сервер транзита интерфейса 1","iface1"],["Сервер транзита интерфейса 2","iface2"],["Сервер транзита интерфейса 3","iface3"],["Сервер транзита интерфейса 4","iface4"]]);
        add_input(row,"port");
	tbody.appendChild(row);	
}

function add_sim_settings_row()
{
	var tbody = document.getElementById('Settings');
	var row = document.createElement("TR")
	add_input(row,"id");
        add_input(row,"pin");
	add_input(row,"addr");
	add_checkbox(row,"auth");
	add_input(row,"login");
	add_input(row,"password");
	add_checkbox(row,"enable");
	tbody.appendChild(row);	
}

function add_time_jrnl_row()
{
	var tbody = document.getElementById('Jrnl');
	var row = document.createElement("TR")
	add_input(row,"id");
	add_input(row,"oldTime");
	add_input(row,"newTime");
	add_select(row,"source",["Синхронизация(SNTP)","Установка(RTU-327)","Установка(HTTP)","Установка(Текстовый протокол)"]);
	tbody.appendChild(row);	
}

function add_meter_answ_jrnl_row()
{
	var tbody = document.getElementById('Jrnl');
	var row = document.createElement("TR")
	add_input(row,"id");
	add_input(row,"time");
	add_input(row,"idMeter");
	add_custom_select(row,"type",[["Меркурий200",1],["Меркурий203",31],["Меркурий206",32],["Меркурий230",3],["Меркурий225.2",91],["СЕ102",8],["СЕ102М",11],["СЕ301",6],["СЕ303",5],["СЭБ2А",2],["ПСЧ3ТА",17],["СЭТ4ТМ",4],["ПСЧхТМ",10],["Альфа1140",25],["ТОПАЗ",33],["НЕВА1xx",26],["НЕВА3xx",27],["Милур10x",28],["Милур30x",29],["СОЭ55/215",24],["СОЭ55/217",22],["СОЭ55/415",30],["СТЭ561",23],["УМТВ10",9],["Пульсар",93],["FX868",92]]);
	add_input(row,"addr");
	add_custom_select(row,"iface",[["Интерфейс 1",0],["Интерфейс 2",1],["Интерфейс 3",2],["Интерфейс 4",3],["Интерфейс 5",4], ["Интерфейс концентратора",6]]);
	add_checkbox(row,"answer");
	tbody.appendChild(row);	
}

function add_ip_settings_row()
{
	var tbody = document.getElementById('Settings');
	var row = document.createElement("TR")
        add_custom_select(row,"iface",[["Ethernet 1","eth0"],["Ethernet 2","eth1"]]);
	add_input(row,"ip");
	add_input(row,"netmask");
        add_input(row,"gw");
        add_input(row,"dns1");
        add_input(row,"dns2");
        add_checkbox(row,"dhcp");
	tbody.appendChild(row);	
}

function add_charge_process_state_row()
{
	var tbody = document.getElementById('State');
	var row = document.createElement("TR")
	add_input(row,"stationTableId");
	add_input(row,"stationId");
	add_input(row,"time");
	add_input(row,"sessionId");
	add_input(row,"chargeLevel");

	tbody.appendChild(row);	
}

function add_charge_session_state_row()
{
	var tbody = document.getElementById('State');
	var row = document.createElement("TR")
	add_input(row,"stationTableId");
	add_input(row,"stationId");
	add_input(row,"time");
	add_input(row,"sessionId");
	add_input(row,"sessionStatus");
	add_input(row,"stockId");
	add_input(row,"stockGarageId");
	add_input(row,"p");
	add_input(row,"i");
	add_input(row,"u");
	add_input(row,"pSumm");
	add_input(row,"startTime");
	add_input(row,"endTime");
	add_input(row,"startChargeLevel");
	add_input(row,"endChargeLevel");

	tbody.appendChild(row);	
}

function add_charge_station_state_row()
{
	var tbody = document.getElementById('State');
	var row = document.createElement("TR")
	add_input(row,"stationTableId");
	add_input(row,"stationId");
	add_input(row,"time");
	add_input(row,"status");
	add_input(row,"p");
	add_input(row,"i");
	add_input(row,"u");
	add_input(row,"uIn");
	add_input(row,"temp");
	add_input(row,"ap");
	add_input(row,"apDay");
	add_input(row,"errors");
	add_checkbox(row,"errNoVoltage");
	add_checkbox(row,"errLowVoltage");
	add_checkbox(row,"errOverVoltage");
	add_checkbox(row,"errInsulationIn");
	add_checkbox(row,"errPowerOff");
	add_checkbox(row,"errOverTemperature");
	add_checkbox(row,"errOpen");
	add_checkbox(row,"errOverCurrent");
	add_checkbox(row,"errInsulationOut");
	add_checkbox(row,"errFireAlarm");	

	tbody.appendChild(row);	
}

function handleLogin(form) {
	var logindata = {
		password: password.value,
		login: username.value
	};
	var request = new XMLHttpRequest();
	request.open('POST', 'auth');
	request.setRequestHeader('X-Protocol-USPD', '40');
	request.setRequestHeader("Content-type", "application/json");
	request.onreadystatechange = function() {
		if (this.readyState == 4) {
            if (this.status == 200) {
				document.location.href = '/main.html';
            }
			if (this.status == 403)
			{
				redirect_to_home_page();
			}
        }
    }
	request.send(JSON.stringify(logindata));
};

function get_main() {                
    var request = new XMLHttpRequest();
    request.open('GET', 'main.cgi');
	request.setRequestHeader('X-Protocol-USPD', '40');
    request.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200) {
                var response = JSON.parse(this.responseText);
                document.getElementById('tm').innerText = response.time;
            }
			if (this.status == 403)
			{
				redirect_to_home_page();
			}
        }
    }
    request.send(null);
}

function disk_clearing() {
	var settings = {
		  name: document.getElementById('clearname').value,
	};
	var xhr = new XMLHttpRequest();
	xhr.open('POST', '/action/disk/clear');
	xhr.setRequestHeader("Content-type", "application/json");
	xhr.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200) {
            }
			if (this.status == 403)
			{
				redirect_to_home_page();
			}
        }
    }
	xhr.send(JSON.stringify(settings));
};

function parse_time(response) {                
	document.getElementById('time').value = response.time;
	document.getElementById('settime').value = response.time;
	document.getElementById('sync').checked = response.sync;
	document.getElementById('extstate').checked = response.state;
}

function get_time() {
	get_settings('/state/time', parse_time);
}

function set_time() {                
    var settings = {
		  time: document.getElementById('settime').value,
	};
	set_settings('/action/time/set',settings,'PUT');
}

function parse_dout_state(response) {                
	for (var i = 0; i < response.State.length; i++) {
		add_dout_state_row();
		document.getElementById('State').rows[i+1].cells.namedItem("addr").childNodes[0].value = response.State[i].addr;
		document.getElementById('State').rows[i+1].cells.namedItem("state").childNodes[0].value = response.State[i].state;
	}
}

function get_dout_state() {
	get_settings('/state/dout', parse_dout_state);
}

function meter_data_table_clear() {
	for (j = document.getElementById('MeterData').rows.length - 1; j > 0 ; j--)
	{
		document.getElementById('MeterData').deleteRow(j);
	}
}

function state_table_clear() {
	for (j = document.getElementById('State').rows.length - 1; j > 0 ; j--)
	{
		document.getElementById('State').deleteRow(j);
	}
}


function ID_search(params) {
	if (document.getElementById('id').value != "")
	{
		var id = parseInt(document.getElementById('id').value);
		params.ids.push(id);
	}
}

function time_search(params) {
	if ( (document.getElementById("STime").value != "") && (document.getElementById("ETime").value != "") )
	{
		var Time = {
			start: parseInt(document.getElementById("STime").value),
			end: parseInt(document.getElementById("ETime").value)
		}
		params.time.push(Time);
	}
	else if (document.getElementById("STime").value != "")
	{
		var Time = {
			start: parseInt(document.getElementById("STime").value)
		}			
		params.time.push(Time);
	}
	else if (document.getElementById("ETime").value != "")
	{
		var Time = {
			end: parseInt(document.getElementById("ETime").value)
		}
		params.time.push(Time);
	}
}

function energy_tag_search(params) {
	if ((document.getElementById("TagAp")) && (document.getElementById("TagAp").checked))
	{
		for (var i = 0; i <= 4; i++) 
		{
			var Tag = "A+" + i;
			params.tags.push(Tag);
		}
	}
	if ((document.getElementById("TagAm")) && (document.getElementById("TagAm").checked))
	{
		for (var i = 0; i <= 4; i++) 
		{
			var Tag = "A-" + i;
			params.tags.push(Tag);
		}
	}
	if ((document.getElementById("TagRp")) && (document.getElementById("TagRp").checked))
	{
		for (var i = 0; i <= 4; i++) 
		{
			var Tag = "R+" + i;
			params.tags.push(Tag);
		}
	}
	if ((document.getElementById("TagRm")) && (document.getElementById("TagRm").checked))
	{
		for (var i = 0; i <= 4; i++) 
		{
			var Tag = "R-" + i;
			params.tags.push(Tag);
		}
	}
}

function pulse_tag_search(params) {
	if ((document.getElementById("TagPls")) && (document.getElementById("TagPls").checked))
	{
		for (var i = 1; i <= 32; i++) 
		{
			var Tag = "Pls" + i;
			params.tags.push(Tag);
		}
	}
}

function din_tag_search(params) {
	if ((document.getElementById("TagDIn")) && (document.getElementById("TagDIn").checked))
	{
		for (var i = 1; i <= 32; i++) 
		{
			var Tag = "Chnl" + i;
			params.tags.push(Tag);
		}
	}
}

function quality_tag_search(params) {
	if ((document.getElementById("TagU")) && (document.getElementById("TagU").checked))
	{
		var Tag = "UA";
		params.tags.push(Tag);
		var Tag = "UB";
		params.tags.push(Tag);
		var Tag = "UC";
		params.tags.push(Tag);
	}
	if ((document.getElementById("TagI")) && (document.getElementById("TagI").checked))
	{
		var Tag = "IA";
		params.tags.push(Tag);
		var Tag = "IB";
		params.tags.push(Tag);
		var Tag = "IC";
		params.tags.push(Tag);
	}
	if ((document.getElementById("TagP")) && (document.getElementById("TagP").checked))
	{
		var Tag = "PS";
		params.tags.push(Tag);
		var Tag = "PA";
		params.tags.push(Tag);
		var Tag = "PB";
		params.tags.push(Tag);
		var Tag = "PC";
		params.tags.push(Tag);
	}
	if ((document.getElementById("TagQ")) && (document.getElementById("TagQ").checked))
	{
		var Tag = "QS";
		params.tags.push(Tag);
		var Tag = "QA";
		params.tags.push(Tag);
		var Tag = "QB";
		params.tags.push(Tag);
		var Tag = "QC";
		params.tags.push(Tag);
	}
	if ((document.getElementById("TagS")) && (document.getElementById("TagS").checked))
	{
		var Tag = "SS";
		params.tags.push(Tag);
		var Tag = "SA";
		params.tags.push(Tag);
		var Tag = "SB";
		params.tags.push(Tag);
		var Tag = "SC";
		params.tags.push(Tag);
	}
	if ((document.getElementById("TagAng")) && (document.getElementById("TagAng").checked))
	{
		var Tag = "AngAB";
		params.tags.push(Tag);
		var Tag = "AngBC";
		params.tags.push(Tag);
		var Tag = "AngAC";
		params.tags.push(Tag);
	}
	if ((document.getElementById("TagkP")) && (document.getElementById("TagkP").checked))
	{
		var Tag = "kPS";
		params.tags.push(Tag);
		var Tag = "kPA";
		params.tags.push(Tag);
		var Tag = "kPB";
		params.tags.push(Tag);
		var Tag = "kPC";
		params.tags.push(Tag);
	}
	if ((document.getElementById("TagFreq")) && (document.getElementById("TagFreq").checked))
	{
		var Tag = "Freq";
		params.tags.push(Tag);
	}
}

function config_tag_search(params) {
}


function cons_tag_search(params) {
	if ((document.getElementById("TagPp")) && (document.getElementById("TagPp").checked))
	{
		var Tag = "P+";
		params.tags.push(Tag);
	}
	if ((document.getElementById("TagPm")) && (document.getElementById("TagPm").checked))
	{
		var Tag = "P-";
		params.tags.push(Tag);
	}
	if ((document.getElementById("TagQp")) && (document.getElementById("TagQp").checked))
	{
		var Tag = "Q+";
		params.tags.push(Tag);
	}
	if ((document.getElementById("TagQm")) && (document.getElementById("TagQm").checked))
	{
		var Tag = "Q-";
		params.tags.push(Tag);
	}
	if ((document.getElementById("TagFlags")) && (document.getElementById("TagFlags").checked))
	{
		var Tag = "isMeas";
		params.tags.push(Tag);
		var Tag = "isSummer";
		params.tags.push(Tag);
		var Tag = "isOvfl";
		params.tags.push(Tag);
		var Tag = "isPart";
		params.tags.push(Tag);
	}
}

function journal_search(params) {
	var Jrnl = document.getElementById("Jrnl").options[document.getElementById("Jrnl").options.selectedIndex].value;
	params.measures.push(Jrnl);
}

function energy_response_parse(response) {
	var idx = 1;
	for (var i = 0; i < response.measures[0].devices.length; i++) {
		if ( response.measures[0].devices[i].error )
				continue;
		if ( !response.measures[0].devices[i].vals )
			continue;
		for (var j = 0; j < response.measures[0].devices[i].vals.length; j++) {
			add_meter_data_eng_row();
			document.getElementById('MeterData').rows[idx].cells.namedItem("id").childNodes[0].value = response.measures[0].devices[i].deviceIdx;
			document.getElementById('MeterData').rows[idx].cells.namedItem("serial").childNodes[0].value = response.measures[0].devices[i].serial;
			document.getElementById('MeterData').rows[idx].cells.namedItem("time").childNodes[0].value = response.measures[0].devices[i].vals[j].ts;
			document.getElementById('MeterData').rows[idx].cells.namedItem("timediff").childNodes[0].value = response.measures[0].devices[i].vals[j].diff;
			if ( response.measures[0].devices[i].vals[j].tags )
			{
				for ( var k = 0; k < response.measures[0].devices[i].vals[j].tags.length; k++)
				{
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "A+0" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Ap0").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "A+1" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Ap1").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "A+2" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Ap2").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "A+3" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Ap3").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "A+4" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Ap4").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "A-0" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Am0").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "A-1" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Am1").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "A-2" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Am2").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "A-3" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Am3").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "A-4" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Am4").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "R+0" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Rp0").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "R+1" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Rp1").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "R+2" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Rp2").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "R+3" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Rp3").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "R+4" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Rp4").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "R-0" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Rm0").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "R-1" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Rm1").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "R-2" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Rm2").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "R-3" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Rm3").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "R-4" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Rm4").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "Pls1" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Ap0").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "Pls2" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Ap1").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "Pls3" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Ap2").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "Pls4" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Ap3").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "Pls5" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Ap4").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "Pls6" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Am0").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "Pls7" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Am1").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "Pls8" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Am2").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "Pls9" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Am3").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "Pls10" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Am4").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "Pls11" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Rp0").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "Pls12" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Rp1").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "Pls13" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Rp2").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "Pls14" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Rp3").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "Pls15" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Rp4").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "Pls16" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Rm0").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "Pls17" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Rm1").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "Pls18" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Rm2").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "Pls19" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Rm3").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "Pls20" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Rm4").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
				}
			}
			idx++;
		}
	}
}

function din_response_parse(response) {
	var idx = 1;
	for (var i = 0; i < response.measures[0].devices.length; i++) {
		if ( response.measures[0].devices[i].error )
				continue;
		if ( !response.measures[0].devices[i].vals )
			continue;
		for (var j = 0; j < response.measures[0].devices[i].vals.length; j++) {
			add_meter_data_din_row();
			document.getElementById('MeterData').rows[idx].cells.namedItem("id").childNodes[0].value = response.measures[0].devices[i].deviceIdx;
			document.getElementById('MeterData').rows[idx].cells.namedItem("serial").childNodes[0].value = response.measures[0].devices[i].serial;
			document.getElementById('MeterData').rows[idx].cells.namedItem("time").childNodes[0].value = response.measures[0].devices[i].vals[j].ts;
			document.getElementById('MeterData').rows[idx].cells.namedItem("timediff").childNodes[0].value = response.measures[0].devices[i].vals[j].diff;
			if ( response.measures[0].devices[i].vals[j].tags )
			{
				for ( var k = 0; k < response.measures[0].devices[i].vals[j].tags.length; k++)
				{		
					document.getElementById('MeterData').rows[idx].cells.namedItem(response.measures[0].devices[i].vals[j].tags[k].tag).childNodes[0].checked = response.measures[0].devices[i].vals[j].tags[k].val;
				}
			}
			idx++;
		}
	}
}

function quality_response_parse(response) {
	var idx = 1;
	for (var i = 0; i < response.measures[0].devices.length; i++) {
		if ( response.measures[0].devices[i].error )
				continue;
		if ( !response.measures[0].devices[i].vals )
			continue;				
		for (var j = 0; j < response.measures[0].devices[i].vals.length; j++) {			
			add_meter_data_qual_row();
			document.getElementById('MeterData').rows[idx].cells.namedItem("id").childNodes[0].value = response.measures[0].devices[i].deviceIdx;
			document.getElementById('MeterData').rows[idx].cells.namedItem("serial").childNodes[0].value = response.measures[0].devices[i].serial;
			document.getElementById('MeterData').rows[idx].cells.namedItem("time").childNodes[0].value = response.measures[0].devices[i].vals[j].ts;
			document.getElementById('MeterData').rows[idx].cells.namedItem("timediff").childNodes[0].value = response.measures[0].devices[i].vals[j].diff;
			if ( response.measures[0].devices[i].vals[j].tags )
			{
				for ( var k = 0; k < response.measures[0].devices[i].vals[j].tags.length; k++)
				{
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "UA" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("UA").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "UB" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("UB").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "UC" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("UC").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "IA" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("IA").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "IB" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("IB").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "IC" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("IC").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "PS" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("PS").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "PA" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("PA").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "PB" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("PB").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "PC" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("PC").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "QS" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("QS").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "QA" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("QA").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "QB" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("QB").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "QC" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("QC").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "SS" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("SS").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "SA" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("SA").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "SB" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("SB").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "SC" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("SC").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "AngAB" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("AngAB").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "AngBC" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("AngBC").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "AngAC" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("AngAC").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "kPS" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("kPS").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "kPA" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("kPA").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "kPB" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("kPB").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "kPC" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("kPC").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "Freq" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Freq").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
				}
			}
			idx++;
		}
	}
}

function config_response_parse(response) {
	var idx = 1;
	for (var i = 0; i < response.measures[0].devices.length; i++) {
		if ( response.measures[0].devices[i].error )
				continue;
		if ( !response.measures[0].devices[i].vals )
			continue;				
		for (var j = 0; j < response.measures[0].devices[i].vals.length; j++) {			
			add_meter_data_config_row();
			document.getElementById('MeterData').rows[idx].cells.namedItem("id").childNodes[0].value = response.measures[0].devices[i].deviceIdx;
			document.getElementById('MeterData').rows[idx].cells.namedItem("serial").childNodes[0].value = response.measures[0].devices[i].serial;
			document.getElementById('MeterData').rows[idx].cells.namedItem("time").childNodes[0].value = response.measures[0].devices[i].vals[j].ts;
			document.getElementById('MeterData').rows[idx].cells.namedItem("timediff").childNodes[0].value = response.measures[0].devices[i].vals[j].diff;
			if ( response.measures[0].devices[i].vals[j].tags )
			{
				for ( var k = 0; k < response.measures[0].devices[i].vals[j].tags.length; k++)
				{
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "kU" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("kU").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "kI" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("kI").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "Const" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Const").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "cTime" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("cTime").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "isDst" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("isDst").childNodes[0].checked = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "isCons" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("isCons").childNodes[0].checked = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "isClock" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("isClock").childNodes[0].checked = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "isTrf" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("isTrf").childNodes[0].checked = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "isAm" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("isAm").childNodes[0].checked = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "isRm" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("isRm").childNodes[0].checked = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "isRp" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("isRp").childNodes[0].checked = response.measures[0].devices[i].vals[j].tags[k].val;
				}
			}
			idx++;
		}
	}
}

function cons_response_parse(response) {
	var idx = 1;
	for (var i = 0; i < response.measures[0].devices.length; i++) {
		if ( response.measures[0].devices[i].error )
				continue;
		if ( !response.measures[0].devices[i].vals )
			continue;				
		for (var j = 0; j < response.measures[0].devices[i].vals.length; j++) {			
			add_meter_data_cons_row();
			document.getElementById('MeterData').rows[idx].cells.namedItem("id").childNodes[0].value = response.measures[0].devices[i].deviceIdx;
			document.getElementById('MeterData').rows[idx].cells.namedItem("serial").childNodes[0].value = response.measures[0].devices[i].serial;
			document.getElementById('MeterData').rows[idx].cells.namedItem("time").childNodes[0].value = response.measures[0].devices[i].vals[j].ts;
			document.getElementById('MeterData').rows[idx].cells.namedItem("timediff").childNodes[0].value = response.measures[0].devices[i].vals[j].diff;
			if ( response.measures[0].devices[i].vals[j].tags )
			{
				for ( var k = 0; k < response.measures[0].devices[i].vals[j].tags.length; k++)
				{
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "P+" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Pp").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "Q+" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Qp").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "P-" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Pm").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "Q-" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("Qm").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "isMeas" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("isMeas").childNodes[0].checked = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "isSummer" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("isSummer").childNodes[0].checked = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "isOvfl" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("isOvfl").childNodes[0].checked = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "isPart" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("isPart").childNodes[0].checked = response.measures[0].devices[i].vals[j].tags[k].val;
				}
			}
			idx++;
		}
	}
}

function journal_response_parse(response) {
	var idx = 1;
	for (var i = 0; i < response.measures[0].devices.length; i++) {
		if ( response.measures[0].devices[i].error )
				continue;
		if ( !response.measures[0].devices[i].vals )
			continue;				
		for (var j = 0; j < response.measures[0].devices[i].vals.length; j++) {
			add_meter_data_journal_row();
			document.getElementById('MeterData').rows[idx].cells.namedItem("id").childNodes[0].value = response.measures[0].devices[i].deviceIdx;
			document.getElementById('MeterData').rows[idx].cells.namedItem("serial").childNodes[0].value = response.measures[0].devices[i].serial;
			document.getElementById('MeterData').rows[idx].cells.namedItem("type").childNodes[0].value = response.measures[0].measure;
			document.getElementById('MeterData').rows[idx].cells.namedItem("time").childNodes[0].value = response.measures[0].devices[i].vals[j].ts;
			document.getElementById('MeterData').rows[idx].cells.namedItem("timediff").childNodes[0].value = response.measures[0].devices[i].vals[j].diff;
			if ( response.measures[0].devices[i].vals[j].tags )
			{
				for ( var k = 0; k < response.measures[0].devices[i].vals[j].tags.length; k++)
				{
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "eventId" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("eId").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "event" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("etype").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
				}
			}
			idx++;
		}
	}
}

function relay_response_parse(response) {
	var idx = 1;
	for (var i = 0; i < response.measures[0].devices.length; i++) {
		if ( response.measures[0].devices[i].error )
				continue;
		if ( !response.measures[0].devices[i].vals )
			continue;				
		for (var j = 0; j < response.measures[0].devices[i].vals.length; j++) {
			add_meter_data_relay_row();
			document.getElementById('MeterData').rows[idx].cells.namedItem("id").childNodes[0].value = response.measures[0].devices[i].deviceIdx;
			document.getElementById('MeterData').rows[idx].cells.namedItem("serial").childNodes[0].value = response.measures[0].devices[i].serial;
			document.getElementById('MeterData').rows[idx].cells.namedItem("time").childNodes[0].value = response.measures[0].devices[i].vals[j].ts;
			document.getElementById('MeterData').rows[idx].cells.namedItem("timediff").childNodes[0].value = response.measures[0].devices[i].vals[j].diff;
			if ( response.measures[0].devices[i].vals[j].tags )
			{
				for ( var k = 0; k < response.measures[0].devices[i].vals[j].tags.length; k++)
				{
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "relayId" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("rId").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
					if ( response.measures[0].devices[i].vals[j].tags[k].tag == "relayState" )
						document.getElementById('MeterData').rows[idx].cells.namedItem("state").childNodes[0].value = response.measures[0].devices[i].vals[j].tags[k].val;
				}
			}
			idx++;
		}
	}
}

function time_response_parse(response) {
	var idx = 1;
	for (var i = 0; i < response.measures[0].devices.length; i++) {
		if ( response.measures[0].devices[i].error )
				continue;
		if ( !response.measures[0].devices[i].vals )
			continue;
		for (var j = 0; j < response.measures[0].devices[i].vals.length; j++) {
			add_meter_data_time_row();
			document.getElementById('MeterData').rows[idx].cells.namedItem("id").childNodes[0].value = response.measures[0].devices[i].deviceIdx;
			document.getElementById('MeterData').rows[idx].cells.namedItem("serial").childNodes[0].value = response.measures[0].devices[i].serial;
			document.getElementById('MeterData').rows[idx].cells.namedItem("time").childNodes[0].value = response.measures[0].devices[i].vals[j].ts;
			document.getElementById('MeterData').rows[idx].cells.namedItem("timediff").childNodes[0].value = response.measures[0].devices[i].vals[j].diff;
			idx++;
		}
	}
}

function get_meter_moment_energy() {  
	var params = {
		ids:[],
		tags:[],
		measures:[]
	};
	params.measures.push("ElMomentEnergy");
	ID_search(params);
	energy_tag_search(params);
	pulse_tag_search(params);
    var request = new XMLHttpRequest();
    request.open('POST', 'meter/data/moment');
	request.setRequestHeader('X-Protocol-USPD', '40');
	meter_data_table_clear();
    request.onreadystatechange = function() {
        if (this.readyState == 4) {
            if ( this.status == 200) {
				energy_response_parse(JSON.parse(this.responseText));				
            }
			if (this.status == 403)
			{
				redirect_to_home_page();
			}
        }
    }
    request.send(JSON.stringify(params));
}

function get_meter_moment_din() {  
	var params = {
		ids:[],
		tags:[],
		measures:[]
	};
	params.measures.push("DigMomentState");
	ID_search(params);
	din_tag_search(params);
    var request = new XMLHttpRequest();
    request.open('POST', 'meter/data/moment');
	request.setRequestHeader('X-Protocol-USPD', '40');
	meter_data_table_clear();
    request.onreadystatechange = function() {
        if (this.readyState == 4) {
            if ( this.status == 200) {
				din_response_parse(JSON.parse(this.responseText));				
            }
			if (this.status == 403)
			{
				redirect_to_home_page();
			}
        }
    }
    request.send(JSON.stringify(params));
}

function get_meter_arch_din() {  
	var params = {
		ids:[],
		tags:[],
		measures:[]
	};
	params.measures.push("DigMomentState");
	ID_search(params);
	din_tag_search(params);
    var request = new XMLHttpRequest();
    request.open('POST', 'meter/data/arch');
	request.setRequestHeader('X-Protocol-USPD', '40');
	meter_data_table_clear();
    request.onreadystatechange = function() {
        if (this.readyState == 4) {
            if ( this.status == 200) {
				din_response_parse(JSON.parse(this.responseText));				
            }
			if (this.status == 403)
			{
				redirect_to_home_page();
			}
        }
    }
    request.send(JSON.stringify(params));
}

function get_meter_jrnl_din() {  
	var params = {
		ids:[],
		tags:[],
		measures:[]
	};
	params.measures.push("DigJournalState");
	ID_search(params);
	din_tag_search(params);
    var request = new XMLHttpRequest();
    request.open('POST', 'meter/data/arch');
	request.setRequestHeader('X-Protocol-USPD', '40');
	meter_data_table_clear();
    request.onreadystatechange = function() {
        if (this.readyState == 4) {
            if ( this.status == 200) {
				din_response_parse(JSON.parse(this.responseText));				
            }
			if (this.status == 403)
			{
				redirect_to_home_page();
			}
        }
    }
    request.send(JSON.stringify(params));
}

function get_meter_moment_quality() {  
	var params = {
		ids:[],
		tags:[],
		measures:[]
	};
	params.measures.push("ElMomentQuality");
	ID_search(params);
	quality_tag_search(params);
    var request = new XMLHttpRequest();
    request.open('POST', 'meter/data/moment');
	request.setRequestHeader('X-Protocol-USPD', '40');
	meter_data_table_clear();
    request.onreadystatechange = function() {
        if (this.readyState == 4) {
            if ( this.status == 200) {
				quality_response_parse(JSON.parse(this.responseText));				
            }
			if (this.status == 403)
			{
				redirect_to_home_page();
			}
        }
    }
    request.send(JSON.stringify(params));
}

function get_meter_arch_energy() {  
	var params = {
		ids:[],
		time:[],
		tags:[],
		measures:[]
	};
	params.measures.push("ElMomentEnergy");
	ID_search(params);
	time_search(params);
	energy_tag_search(params);
	pulse_tag_search(params);
    var request = new XMLHttpRequest();
    request.open('POST', 'meter/data/arch');
	request.setRequestHeader('X-Protocol-USPD', '40');
	meter_data_table_clear();
    request.onreadystatechange = function() {
        if (this.readyState == 4) {
            if ( this.status == 200) {
				energy_response_parse(JSON.parse(this.responseText));
            }
			if (this.status == 403)
			{
				redirect_to_home_page();
			}
        }
    }
    request.send(JSON.stringify(params));
}

function get_meter_arch_quality() {  
	var params = {
		ids:[],
		time:[],
		tags:[],
		measures:[]
	};
	params.measures.push("ElMomentQuality");
	ID_search(params);
	time_search(params);
	quality_tag_search(params);
    var request = new XMLHttpRequest();
    request.open('POST', 'meter/data/arch');
	request.setRequestHeader('X-Protocol-USPD', '40');
	meter_data_table_clear();
    request.onreadystatechange = function() {
        if (this.readyState == 4) {
            if ( this.status == 200) {
				quality_response_parse(JSON.parse(this.responseText));
            }
			if (this.status == 403)
			{
				redirect_to_home_page();
			}
        }
    }
    request.send(JSON.stringify(params));
}

function get_meter_arch_day() {  
	var params = {
		ids:[],
		time:[],
		tags:[],
		measures:[]
	};
	params.measures.push("ElDayEnergy");
	ID_search(params);
	time_search(params);
	energy_tag_search(params);
	pulse_tag_search(params);
    var request = new XMLHttpRequest();
    request.open('POST', 'meter/data/arch');
	request.setRequestHeader('X-Protocol-USPD', '40');
	meter_data_table_clear();
    request.onreadystatechange = function() {
        if (this.readyState == 4) {
            if ( this.status == 200) {
				energy_response_parse(JSON.parse(this.responseText));
            }
			if (this.status == 403)
			{
				redirect_to_home_page();
			}
        }
    }
    request.send(JSON.stringify(params));
}

function get_meter_arch_day_cons() {  
	var params = {
		ids:[],
		time:[],
		tags:[],
		measures:[]
	};
	params.measures.push("ElDayConsEnergy");
	ID_search(params);
	time_search(params);
	energy_tag_search(params);
	pulse_tag_search(params);
    var request = new XMLHttpRequest();
    request.open('POST', 'meter/data/arch');
	request.setRequestHeader('X-Protocol-USPD', '40');
	meter_data_table_clear();
    request.onreadystatechange = function() {
        if (this.readyState == 4) {
            if ( this.status == 200) {
				energy_response_parse(JSON.parse(this.responseText));
            }
			if (this.status == 403)
			{
				redirect_to_home_page();
			}
        }
    }
    request.send(JSON.stringify(params));
}

function get_meter_arch_month() {  
	var params = {
		ids:[],
		time:[],
		tags:[],
		measures:[]
	};
	params.measures.push("ElMonthEnergy");
	ID_search(params);
	time_search(params);
	energy_tag_search(params);
	pulse_tag_search(params);
    var request = new XMLHttpRequest();
    request.open('POST', 'meter/data/arch');
	request.setRequestHeader('X-Protocol-USPD', '40');
	meter_data_table_clear();
    request.onreadystatechange = function() {
        if (this.readyState == 4) {
            if ( this.status == 200) {
				energy_response_parse(JSON.parse(this.responseText));
            }
			if (this.status == 403)
			{
				redirect_to_home_page();
			}
        }
    }
    request.send(JSON.stringify(params));
}

function get_meter_arch_month_cons() {  
	var params = {
		ids:[],
		time:[],
		tags:[],
		measures:[]
	};
	params.measures.push("ElMonthConsEnergy");
	ID_search(params);
	time_search(params);
	energy_tag_search(params);
	pulse_tag_search(params);
    var request = new XMLHttpRequest();
    request.open('POST', 'meter/data/arch');
	request.setRequestHeader('X-Protocol-USPD', '40');
	meter_data_table_clear();
    request.onreadystatechange = function() {
        if (this.readyState == 4) {
            if ( this.status == 200) {
				energy_response_parse(JSON.parse(this.responseText));
            }
			if (this.status == 403)
			{
				redirect_to_home_page();
			}
        }
    }
    request.send(JSON.stringify(params));
}

function get_meter_arch_config() {  
	var params = {
		ids:[],
		time:[],
		tags:[],
		measures:[]
	};
	params.measures.push("ElConfig");
	ID_search(params);
	time_search(params);
	config_tag_search(params);
    var request = new XMLHttpRequest();
    request.open('POST', 'meter/data/arch');
	request.setRequestHeader('X-Protocol-USPD', '40');
	meter_data_table_clear();
    request.onreadystatechange = function() {
        if (this.readyState == 4) {
            if ( this.status == 200) {
				config_response_parse(JSON.parse(this.responseText));
            }
			if (this.status == 403)
			{
				redirect_to_home_page();
			}
        }
    }
    request.send(JSON.stringify(params));
}

function get_meter_arch_cons() {  
	var params = {
		ids:[],
		time:[],
		tags:[],
		measures:[]
	};
	params.measures.push("ElArr1ConsPower");
	ID_search(params);
	time_search(params);
	cons_tag_search(params);
	pulse_tag_search(params);
    var request = new XMLHttpRequest();
    request.open('POST', 'meter/data/arch');
	request.setRequestHeader('X-Protocol-USPD', '40');
	meter_data_table_clear();
    request.onreadystatechange = function() {
        if (this.readyState == 4) {
            if ( this.status == 200) {
				cons_response_parse(JSON.parse(this.responseText));
            }
			if (this.status == 403)
			{
				redirect_to_home_page();
			}
        }
    }
    request.send(JSON.stringify(params));
}

function get_meter_arch_hour() {  
	var params = {
		ids:[],
		time:[],
		tags:[],
		measures:[]
	};
	params.measures.push("PlsHourPulse");
	ID_search(params);
	time_search(params);
	energy_tag_search(params);
	pulse_tag_search(params);
    var request = new XMLHttpRequest();
    request.open('POST', 'meter/data/arch');
	request.setRequestHeader('X-Protocol-USPD', '40');
	meter_data_table_clear();
    request.onreadystatechange = function() {
        if (this.readyState == 4) {
            if ( this.status == 200) {
				energy_response_parse(JSON.parse(this.responseText));
            }
			if (this.status == 403)
			{
				redirect_to_home_page();
			}
        }
    }
    request.send(JSON.stringify(params));
}

function get_meter_jrnl() {  
	var params = {
		ids:[],
		time:[],
		measures:[]
	};
	ID_search(params);
	time_search(params);
	journal_search(params);
    var request = new XMLHttpRequest();
    request.open('POST', 'meter/data/arch');
	request.setRequestHeader('X-Protocol-USPD', '40');
	meter_data_table_clear();
    request.onreadystatechange = function() {
        if (this.readyState == 4) {
            if ( this.status == 200) {
				journal_response_parse(JSON.parse(this.responseText));
            }
			if (this.status == 403)
			{
				redirect_to_home_page();
			}
        }
    }
    request.send(JSON.stringify(params));
}

function get_meter_moment_time() {  
	var params = {
		ids:[],
		measures:[]
	};
	params.measures.push("GetTime");
	ID_search(params);
    var request = new XMLHttpRequest();
    request.open('POST', 'meter/data/moment');
	request.setRequestHeader('X-Protocol-USPD', '40');
	meter_data_table_clear();
    request.onreadystatechange = function() {
        if (this.readyState == 4) {
            if ( this.status == 200) {
				time_response_parse(JSON.parse(this.responseText));				
            }
			if (this.status == 403)
			{
				redirect_to_home_page();
			}
        }
    }
    request.send(JSON.stringify(params));
}

function get_meter_moment_relay() {  
	var params = {
		ids:[],
		measures:[]
	};
	params.measures.push("GetRelay");
	ID_search(params);
    var request = new XMLHttpRequest();
    request.open('POST', 'meter/data/moment');
	request.setRequestHeader('X-Protocol-USPD', '40');
	meter_data_table_clear();
    request.onreadystatechange = function() {
        if (this.readyState == 4) {
            if ( this.status == 200) {
				relay_response_parse(JSON.parse(this.responseText));				
            }
			if (this.status == 403)
			{
				redirect_to_home_page();
			}
        }
    }
    request.send(JSON.stringify(params));
}

function parse_time_jrnl(response) {                
	for (var i = 0; i < response.Jrnl.length; i++) {
		add_time_jrnl_row();
		document.getElementById('Jrnl').rows[i+1].cells.namedItem("id").childNodes[0].value = response.Jrnl[i].id;
		document.getElementById('Jrnl').rows[i+1].cells.namedItem("oldTime").childNodes[0].value = response.Jrnl[i].oldTime;
		document.getElementById('Jrnl').rows[i+1].cells.namedItem("newTime").childNodes[0].value = response.Jrnl[i].newTime;
		document.getElementById('Jrnl').rows[i+1].cells.namedItem("source").childNodes[0].value = response.Jrnl[i].source;
	}
}

function get_time_jrnl() {
	get_settings('/jrnl/time', parse_time_jrnl);
}
	
function parse_meter_answ_jrnl(response) {                
	for (var i = 0; i < response.Jrnl.length; i++) {
		add_meter_answ_jrnl_row();
		document.getElementById('Jrnl').rows[i+1].cells.namedItem("id").childNodes[0].value = response.Jrnl[i].id;
		document.getElementById('Jrnl').rows[i+1].cells.namedItem("time").childNodes[0].value = response.Jrnl[i].time;
		document.getElementById('Jrnl').rows[i+1].cells.namedItem("idMeter").childNodes[0].value = response.Jrnl[i].idMeter;
		document.getElementById('Jrnl').rows[i+1].cells.namedItem("type").childNodes[0].value = response.Jrnl[i].type;
		document.getElementById('Jrnl').rows[i+1].cells.namedItem("addr").childNodes[0].value = response.Jrnl[i].addr;
		document.getElementById('Jrnl').rows[i+1].cells.namedItem("iface").childNodes[0].value = response.Jrnl[i].iface;
		document.getElementById('Jrnl').rows[i+1].cells.namedItem("answer").childNodes[0].checked = response.Jrnl[i].answer;
	}
}

function get_meter_answ_jrnl() {
	get_settings('/jrnl/meter/answ', parse_meter_answ_jrnl);
}

function parse_json_auth_settings(response) {
	for (var i = 0; i < response.Settings.length; i++) {
		add_json_auth_settings_row();
		document.getElementById('Settings').rows[i+1].cells.namedItem("id").childNodes[0].value = response.Settings[i].id;
		document.getElementById('Settings').rows[i+1].cells.namedItem("login").childNodes[0].value = response.Settings[i].login;
		document.getElementById('Settings').rows[i+1].cells.namedItem("password").childNodes[0].value = response.Settings[i].password;
		document.getElementById('Settings').rows[i+1].cells.namedItem("lvl").childNodes[0].value = response.Settings[i].lvl;
	}
}

function get_json_auth_settings() {
	get_settings('/settings/proto/json/auth', parse_json_auth_settings);
}

function set_json_auth_settings() {
	var settings = {
		Settings:[]
	};
	for ( i = 0; i < document.getElementById("Settings").rows.length - 1; i++ )
	{
		if (document.getElementById('Settings').rows[i+1].cells.namedItem("id").childNodes[0].value != "")
		{			
			var setting = { 					
					id: parseInt(document.getElementById('Settings').rows[i+1].cells.namedItem("id").childNodes[0].value), 
					login: document.getElementById('Settings').rows[i+1].cells.namedItem("login").childNodes[0].value,
					password: document.getElementById('Settings').rows[i+1].cells.namedItem("password").childNodes[0].value,
					lvl: parseInt(document.getElementById('Settings').rows[i+1].cells.namedItem("lvl").childNodes[0].value), 					
				}
			settings.Settings.push(setting);
		}
	}
	set_settings('/settings/proto/json/auth',settings,'PUT');
};

function del_json_auth_settings() {
	var settings = {
		Settings:[]
	};
	for ( i = 0; i < document.getElementById("Settings").rows.length - 1; i++ )
	{
		if (document.getElementById('Settings').rows[i+1].cells.namedItem("id").childNodes[0].value != "")
		{			
			var setting = { 					
					id: parseInt(document.getElementById('Settings').rows[i+1].cells.namedItem("id").childNodes[0].value), 				
				}
			settings.Settings.push(setting);
		}
	}
	set_settings('/settings/proto/json/auth',settings,'DELETE');
};

function parse_ip_settings(response) {
	for (var i = 0; i < response.Settings.length; i++) {
			add_ip_settings_row();
			document.getElementById('Settings').rows[i+1].cells.namedItem("iface").childNodes[0].value = response.Settings[i].iface;
			document.getElementById('Settings').rows[i+1].cells.namedItem("ip").childNodes[0].value = response.Settings[i].ip;
			document.getElementById('Settings').rows[i+1].cells.namedItem("netmask").childNodes[0].value = response.Settings[i].netmask;
			document.getElementById('Settings').rows[i+1].cells.namedItem("gw").childNodes[0].value = response.Settings[i].gw;
			document.getElementById('Settings').rows[i+1].cells.namedItem("dns1").childNodes[0].value = response.Settings[i].dns1;
			document.getElementById('Settings').rows[i+1].cells.namedItem("dns2").childNodes[0].value = response.Settings[i].dns2;
			document.getElementById('Settings').rows[i+1].cells.namedItem("dhcp").childNodes[0].checked = response.Settings[i].dhcp;
	}
}

function get_ip_settings() {
	get_settings('/settings/ip', parse_ip_settings);
}

function set_ip_settings() {
	var settings = {
		Settings:[]
	};
	for ( i = 0; i < document.getElementById("Settings").rows.length - 1; i++ )
	{
		var setting = { 
				iface: document.getElementById('Settings').rows[i+1].cells.namedItem("iface").childNodes[0].value, 
				ip: document.getElementById('Settings').rows[i+1].cells.namedItem("ip").childNodes[0].value,					
				netmask: document.getElementById('Settings').rows[i+1].cells.namedItem("netmask").childNodes[0].value,
				gw: document.getElementById('Settings').rows[i+1].cells.namedItem("gw").childNodes[0].value,
				dns1: document.getElementById('Settings').rows[i+1].cells.namedItem("dns1").childNodes[0].value,
				dns2: document.getElementById('Settings').rows[i+1].cells.namedItem("dns2").childNodes[0].value,
				dhcp: document.getElementById('Settings').rows[i+1].cells.namedItem("dhcp").childNodes[0].checked
			}
		settings.Settings.push(setting);
	}
	set_settings('/settings/ip',settings,'PUT');
};

function parse_uart_settings(response) {                
	for (var i = 0; i < response.Settings.length; i++) {
		add_uart_settings_row();
		document.getElementById('Settings').rows[i+1].cells.namedItem("id").childNodes[0].value = response.Settings[i].id;
		document.getElementById('Settings').rows[i+1].cells.namedItem("iface").childNodes[0].value = response.Settings[i].iface;
		document.getElementById('Settings').rows[i+1].cells.namedItem("line").childNodes[0].value = response.Settings[i].line;
		document.getElementById('Settings').rows[i+1].cells.namedItem("br").childNodes[0].value = response.Settings[i].br;
		document.getElementById('Settings').rows[i+1].cells.namedItem("size").childNodes[0].value = response.Settings[i].size;
		document.getElementById('Settings').rows[i+1].cells.namedItem("parity").childNodes[0].value = response.Settings[i].parity;
		document.getElementById('Settings').rows[i+1].cells.namedItem("stop").childNodes[0].value = response.Settings[i].stop;
	}
}

function get_uart_settings() {
	get_settings('/settings/uart', parse_uart_settings);
}

function set_uart_settings() {
	var settings = {
		Settings:[]
	};
	for ( i = 0; i < document.getElementById("Settings").rows.length - 1; i++ )
	{
		if (document.getElementById('Settings').rows[i+1].cells.namedItem("id").childNodes[0].value != "")
		{
			var setting = { 
					id: parseInt(document.getElementById('Settings').rows[i+1].cells.namedItem("id").childNodes[0].value), 
					iface: parseInt(document.getElementById('Settings').rows[i+1].cells.namedItem("iface").childNodes[0].value),					
					br: parseInt(document.getElementById('Settings').rows[i+1].cells.namedItem("br").childNodes[0].value),
					size: parseInt(document.getElementById('Settings').rows[i+1].cells.namedItem("size").childNodes[0].value),
					parity: parseInt(document.getElementById('Settings').rows[i+1].cells.namedItem("parity").childNodes[0].value),
					stop: parseInt(document.getElementById('Settings').rows[i+1].cells.namedItem("stop").childNodes[0].value),
					line: parseInt(document.getElementById('Settings').rows[i+1].cells.namedItem("line").childNodes[0].value)
				}
			settings.Settings.push(setting);
		}
	}
	set_settings('/settings/uart',settings,'PUT');
};

function del_uart_settings() {
	del_settings('/settings/uart');
};

function parse_dout_settings(response) {                
	for (var i = 0; i < response.Settings.length; i++) {
		add_dout_settings_row();
		document.getElementById('Settings').rows[i+1].cells.namedItem("addr").childNodes[0].value = response.Settings[i].addr;
		document.getElementById('Settings').rows[i+1].cells.namedItem("state").childNodes[0].value = response.Settings[i].state;
	}
}

function get_dout_settings() {
	get_settings('/settings/dout', parse_dout_settings);
}

function set_dout_settings() {
	var settings = {
		Settings:[]
	};
	for ( i = 0; i < document.getElementById("Settings").rows.length - 1; i++ )
	{		
			var setting = { 					
					addr: document.getElementById('Settings').rows[i+1].cells.namedItem("addr").childNodes[0].value,
					state: document.getElementById('Settings').rows[i+1].cells.namedItem("state").childNodes[0].value,					
				}
			settings.Settings.push(setting);
	}
	set_settings('/settings/dout',settings,'PUT');
};

function del_dout_settings() {
	del_settings('/settings/dout');
};

function parse_local_time_settings(response) {                
	document.getElementById('tz').value = response.tz;
}

function get_local_time_settings() {
	get_settings('/settings/time/local', parse_local_time_settings);
}

function set_local_time_settings() {
	var settings = {
		  tz: Number(document.getElementById('tz').value),
	};
	set_settings('/settings/time/local',settings,'PUT');
};

function parse_sim_settings(response) {                
	for (var i = 0; i < response.Settings.length; i++) {
		add_sim_settings_row();
		document.getElementById('Settings').rows[i+1].cells.namedItem("id").childNodes[0].value = response.Settings[i].id;
                document.getElementById('Settings').rows[i+1].cells.namedItem("pin").childNodes[0].value = response.Settings[i].pin;
		document.getElementById('Settings').rows[i+1].cells.namedItem("addr").childNodes[0].value = response.Settings[i].addr;
		document.getElementById('Settings').rows[i+1].cells.namedItem("auth").childNodes[0].checked = response.Settings[i].auth;
		document.getElementById('Settings').rows[i+1].cells.namedItem("login").childNodes[0].value = response.Settings[i].login;
		document.getElementById('Settings').rows[i+1].cells.namedItem("password").childNodes[0].value = response.Settings[i].password;
		document.getElementById('Settings').rows[i+1].cells.namedItem("enable").childNodes[0].checked = response.Settings[i].enable;
	}
}

function get_sim_settings() {
	get_settings('/settings/modem/sim', parse_sim_settings);
}

function set_sim_settings() {
	var settings = {
		Settings:[]
	};
	for ( i = 0; i < document.getElementById("Settings").rows.length - 1; i++ )
	{
		if (document.getElementById('Settings').rows[i+1].cells.namedItem("id").childNodes[0].value != "")
		{			
			var setting = { 					
					id: parseInt(document.getElementById('Settings').rows[i+1].cells.namedItem("id").childNodes[0].value), 
					pin: document.getElementById('Settings').rows[i+1].cells.namedItem("pin").childNodes[0].value,
                                        addr: document.getElementById('Settings').rows[i+1].cells.namedItem("addr").childNodes[0].value,
					auth: document.getElementById('Settings').rows[i+1].cells.namedItem("auth").childNodes[0].checked,			
					login: document.getElementById('Settings').rows[i+1].cells.namedItem("login").childNodes[0].value,					
					password: document.getElementById('Settings').rows[i+1].cells.namedItem("password").childNodes[0].value,			
					enable: document.getElementById('Settings').rows[i+1].cells.namedItem("enable").childNodes[0].checked,			
				}
			settings.Settings.push(setting);
		}
	}
	set_settings('/settings/modem/sim',settings,'PUT');
};

function del_sim_settings() {
	del_settings('/settings/modem/sim');
};

function parse_sntp_settings(response) {                
	for (var i = 0; i < response.Settings.length; i++) {
		add_sntp_srv_row();
		document.getElementById('Settings').rows[i+1].cells.namedItem("addr").childNodes[0].value = response.Settings[i].addr;
	}
}

function get_sntp_settings() {
	get_settings('/settings/servers/sntp', parse_sntp_settings);
}

function set_sntp_settings() {
	var settings = {
		Settings:[]
	};
	for ( i = 0; i < document.getElementById("Settings").rows.length - 1; i++ )
	{
		if (document.getElementById('Settings').rows[i+1].cells.namedItem("addr").childNodes[0].value != "")
		{	
			var setting = { 
				addr: document.getElementById('Settings').rows[i+1].cells.namedItem("addr").childNodes[0].value,
			}
		}
		settings.Settings.push(setting);
	}
	set_settings('/settings/servers/sntp',settings,'PUT');
};

function del_sntp_settings() {
	del_settings('/settings/servers/sntp');
};

function parse_tcp_settings(response) {                
	for (var i = 0; i < response.Settings.length; i++) {
		add_http_srv_row();				
		document.getElementById('Settings').rows[i+1].cells.namedItem("port").childNodes[0].value = response.Settings[i].port;
		document.getElementById('Settings').rows[i+1].cells.namedItem("type").childNodes[0].value = response.Settings[i].type;
	}
}

function get_tcp_settings() {
	get_settings('/settings/servers/tcp', parse_tcp_settings);
}

function set_tcp_settings() {
	var settings = {
		Settings:[]
	};
	for ( i = 0; i < document.getElementById("Settings").rows.length - 1; i++ )
	{
		if (document.getElementById('Settings').rows[i+1].cells.namedItem("port").childNodes[0].value != "")
		{			
			var setting = {	  
				port: parseInt(document.getElementById('Settings').rows[i+1].cells.namedItem("port").childNodes[0].value), 
				type: document.getElementById('Settings').rows[i+1].cells.namedItem("type").childNodes[0].value, 
			}
			settings.Settings.push(setting);
		}
	}
	set_settings('/settings/servers/tcp',settings,'PUT');
};

function del_tcp_settings() {
	del_settings('/settings/servers/tcp');
};

function parse_mqtt_settings(response) {                
	for (var i = 0; i < response.Settings.length; i++) {
		add_mqtt_srv_row();
		document.getElementById('Settings').rows[i+1].cells.namedItem("id").childNodes[0].value = response.Settings[i].id;
		document.getElementById('Settings').rows[i+1].cells.namedItem("addr").childNodes[0].value = response.Settings[i].addr;
		document.getElementById('Settings').rows[i+1].cells.namedItem("port").childNodes[0].value = response.Settings[i].port;
		document.getElementById('Settings').rows[i+1].cells.namedItem("login").childNodes[0].value = response.Settings[i].login;
		document.getElementById('Settings').rows[i+1].cells.namedItem("password").childNodes[0].value = response.Settings[i].password;
		document.getElementById('Settings').rows[i+1].cells.namedItem("prefix").childNodes[0].value = response.Settings[i].prefix;
		document.getElementById('Settings').rows[i+1].cells.namedItem("deviceID").childNodes[0].value = response.Settings[i].deviceID;
		document.getElementById('Settings').rows[i+1].cells.namedItem("cropt").childNodes[0].value = response.Settings[i].cropt;
	}
}

function get_mqtt_settings() {
	get_settings('/settings/servers/mqtt', parse_mqtt_settings);
}

function set_mqtt_settings() {
	var settings = {
		Settings:[]
	};
	for ( i = 0; i < document.getElementById("Settings").rows.length - 1; i++ )
	{
		if (document.getElementById('Settings').rows[i+1].cells.namedItem("id").childNodes[0].value != "")
		{			
			var setting = {	  
				id: parseInt(document.getElementById('Settings').rows[i+1].cells.namedItem("id").childNodes[0].value), 
				addr: document.getElementById('Settings').rows[i+1].cells.namedItem("addr").childNodes[0].value, 
				port: parseInt(document.getElementById('Settings').rows[i+1].cells.namedItem("port").childNodes[0].value), 
				login: document.getElementById('Settings').rows[i+1].cells.namedItem("login").childNodes[0].value, 
				password: document.getElementById('Settings').rows[i+1].cells.namedItem("password").childNodes[0].value,
				prefix: document.getElementById('Settings').rows[i+1].cells.namedItem("prefix").childNodes[0].value,
				deviceID: document.getElementById('Settings').rows[i+1].cells.namedItem("deviceID").childNodes[0].value,
				cropt: parseInt(document.getElementById('Settings').rows[i+1].cells.namedItem("cropt").childNodes[0].value),
			}
			settings.Settings.push(setting);
		}
	}
	set_settings('/settings/servers/mqtt',settings,'PUT');
};


function del_mqtt_settings() {
	del_settings('/settings/servers/mqtt');
};

function parse_meter_template_settings(response) {                
	var outCnt = 0;
	for (var i = 0; i < response.Settings.length; i++) {
		add_meter_template_row();
		outCnt++;
		document.getElementById('Settings').rows[outCnt].cells.namedItem("name").childNodes[0].value = response.Settings[i].name;
		for ( var j = 0; j < response.Settings[i].meters.length; j++)
		{
			add_meter_template_settings_row();
			outCnt++;
			document.getElementById('Settings').rows[outCnt].cells.namedItem("meterId").childNodes[0].value = response.Settings[i].meters[j];
		}
	}
}

function get_meter_template_settings() {
	get_settings('/settings/templates/meter', parse_meter_template_settings);
}

function set_meter_template_settings() {
	var settings = {
		Settings:[]
	};
	for ( i = 0; i < document.getElementById("Settings").rows.length - 1; i++ )
	{
		if ( (document.getElementById('Settings').rows[i+1].cells.namedItem("name") != null) &&
			(document.getElementById('Settings').rows[i+1].cells.namedItem("name").childNodes[0].value != "") )
		{			
			var setting = { 					
				name: document.getElementById('Settings').rows[i+1].cells.namedItem("name").childNodes[0].value,
				meters:[]
			}
			for ( j = i + 1; j < document.getElementById("Settings").rows.length - 1; j++ )
			{
				if (document.getElementById('Settings').rows[j+1].cells.namedItem("name") != null)
					break;
				setting.meters.push(parseInt(document.getElementById('Settings').rows[j+1].cells.namedItem("meterId").childNodes[0].value));
			}			
			settings.Settings.push(setting);
		}		
	}
	set_settings('/settings/templates/meter',settings,'PUT');
};

function del_meter_template_settings() {
	del_settings('/settings/templates/meter');
};

function parse_meter_arch_template_settings(response) {                
	var outCnt = 0;
	for (var i = 0; i < response.Settings.length; i++) {
		add_meter_arch_template_row();
		outCnt++;
		document.getElementById('Settings').rows[outCnt].cells.namedItem("name").childNodes[0].value = response.Settings[i].name;
		for ( var j = 0; j < response.Settings[i].types.length; j++)
		{
			add_meter_arch_template_settings_row();
			outCnt++;
			document.getElementById('Settings').rows[outCnt].cells.namedItem("ArchType").childNodes[0].value = response.Settings[i].types[j];
		}
	}
}

function get_meter_arch_template_settings() {
	get_settings('/settings/templates/arch', parse_meter_arch_template_settings);
}

function set_meter_arch_template_settings() {
	var settings = {
		Settings:[]
	};
	for ( i = 0; i < document.getElementById("Settings").rows.length - 1; i++ )
	{
		if ( (document.getElementById('Settings').rows[i+1].cells.namedItem("name") != null) &&
			(document.getElementById('Settings').rows[i+1].cells.namedItem("name").childNodes[0].value != "") )
		{			
			var setting = { 					
				name: document.getElementById('Settings').rows[i+1].cells.namedItem("name").childNodes[0].value,
				types:[]
			}
			for ( j = i + 1; j < document.getElementById("Settings").rows.length - 1; j++ )
			{
				if (document.getElementById('Settings').rows[j+1].cells.namedItem("name") != null)
					break;
				setting.types.push(document.getElementById('Settings').rows[j+1].cells.namedItem("ArchType").childNodes[0].value);
			}			
			settings.Settings.push(setting);
		}		
	}
	set_settings('/settings/templates/arch',settings,'PUT');
};

function del_meter_arch_template_settings() {
	del_settings('/settings/templates/arch');
};


function parse_meter_tables(response) {                
	for (var i = 0; i < response.Meters.length; i++) {
		add_meter_row();
		document.getElementById('Meters').rows[i+1].cells.namedItem("id").childNodes[0].value = response.Meters[i].id;
		document.getElementById('Meters').rows[i+1].cells.namedItem("pId").childNodes[0].value = response.Meters[i].pId;
		document.getElementById('Meters').rows[i+1].cells.namedItem("type").childNodes[0].value = response.Meters[i].typeName;					
		document.getElementById('Meters').rows[i+1].cells.namedItem("addr").childNodes[0].value = response.Meters[i].addr;
		document.getElementById('Meters').rows[i+1].cells.namedItem("passRd").childNodes[0].value = response.Meters[i].passRd;
		document.getElementById('Meters').rows[i+1].cells.namedItem("passWr").childNodes[0].value = response.Meters[i].passWr;
		document.getElementById('Meters').rows[i+1].cells.namedItem("iface").childNodes[0].value = response.Meters[i].ifaceName;
		document.getElementById('Meters').rows[i+1].cells.namedItem("ifaceCfg").childNodes[0].value = response.Meters[i].ifaceCfg;
		if ( response.Meters[i].rtuObjType )
			document.getElementById('Meters').rows[i+1].cells.namedItem("rtuObjType").childNodes[0].value = response.Meters[i].rtuObjType;
		if ( response.Meters[i].rtuObjNum )
			document.getElementById('Meters').rows[i+1].cells.namedItem("rtuObjNum").childNodes[0].value = response.Meters[i].rtuObjNum;
		if ( response.Meters[i].rtuFider )
			document.getElementById('Meters').rows[i+1].cells.namedItem("rtuFider").childNodes[0].value = response.Meters[i].rtuFider;
	}
}

function get_meter_table() {
	get_settings('/settings/meter/table', parse_meter_tables);
}

function set_meter_table() {
	var settings = {
		Meters:[]
	};
	for ( i = 0; i < document.getElementById("Meters").rows.length - 1; i++ )
	{
		if (document.getElementById('Meters').rows[i+1].cells.namedItem("id").childNodes[0].value != "")
		{
			var setting = { 
					id: parseInt(document.getElementById('Meters').rows[i+1].cells.namedItem("id").childNodes[0].value),
					pId: parseInt(document.getElementById('Meters').rows[i+1].cells.namedItem("pId").childNodes[0].value),
					typeName: document.getElementById('Meters').rows[i+1].cells.namedItem("type").childNodes[0].value,
					addr: document.getElementById('Meters').rows[i+1].cells.namedItem("addr").childNodes[0].value,
					passRd: document.getElementById('Meters').rows[i+1].cells.namedItem("passRd").childNodes[0].value,
					passWr: document.getElementById('Meters').rows[i+1].cells.namedItem("passWr").childNodes[0].value,
					ifaceName: document.getElementById('Meters').rows[i+1].cells.namedItem("iface").childNodes[0].value,
					ifaceCfg: document.getElementById('Meters').rows[i+1].cells.namedItem("ifaceCfg").childNodes[0].value,
					rtuObjType: parseInt(document.getElementById('Meters').rows[i+1].cells.namedItem("rtuObjType").childNodes[0].value),
					rtuObjNum: parseInt(document.getElementById('Meters').rows[i+1].cells.namedItem("rtuObjNum").childNodes[0].value),
					rtuFider: parseInt(document.getElementById('Meters').rows[i+1].cells.namedItem("rtuFider").childNodes[0].value)
				}
			settings.Meters.push(setting);
		}
	}
	set_settings('/settings/meter/table',settings,'PUT');
};

function del_meter_table() {
	del_settings('/settings/meter/table');
};

function parse_charge_station_table(response) {                
	for (var i = 0; i < response.settings.length; i++) {
		add_charge_station_row();
		document.getElementById('ChargeStations').rows[i+1].cells.namedItem("id").childNodes[0].value = response.settings[i].id;
		document.getElementById('ChargeStations').rows[i+1].cells.namedItem("type").childNodes[0].value = response.settings[i].type;
		document.getElementById('ChargeStations').rows[i+1].cells.namedItem("addr").childNodes[0].value = response.settings[i].addr;
		document.getElementById('ChargeStations').rows[i+1].cells.namedItem("port").childNodes[0].value = response.settings[i].port;
		document.getElementById('ChargeStations').rows[i+1].cells.namedItem("mqttId").childNodes[0].value = response.settings[i].mqttId;
	}
}

function get_charge_station_table() {
	get_settings('/settings/charge/table', parse_charge_station_table);
}

function set_charge_station_table() {
	var indata = {
		settings:[]
	};
	for ( i = 0; i < document.getElementById("ChargeStations").rows.length - 1; i++ )
	{
		if (document.getElementById('ChargeStations').rows[i+1].cells.namedItem("id").childNodes[0].value != "")
		{
			var setting = { 
					id: parseInt(document.getElementById('ChargeStations').rows[i+1].cells.namedItem("id").childNodes[0].value),
					type: document.getElementById('ChargeStations').rows[i+1].cells.namedItem("type").childNodes[0].value,
					addr: document.getElementById('ChargeStations').rows[i+1].cells.namedItem("addr").childNodes[0].value,
					port: parseInt(document.getElementById('ChargeStations').rows[i+1].cells.namedItem("port").childNodes[0].value),
					mqttId: parseInt(document.getElementById('ChargeStations').rows[i+1].cells.namedItem("mqttId").childNodes[0].value),
				}
			indata.settings.push(setting);
		}
	}
	set_settings('/settings/charge/table',indata,'PUT');
};

function del_charge_station_table() {
	del_settings('/settings/charge/table');
};

function parse_schdl_event_settings(response) {                
	for (var i = 0; i < response.settings.length; i++) {
		add_schdl_event_row();
		document.getElementById('Settings').rows[i+1].cells.namedItem("id").childNodes[0].value = response.settings[i].id;
		if (response.settings[i].min)
			document.getElementById('Settings').rows[i+1].cells.namedItem("min").childNodes[0].value = response.settings[i].min;
		if (response.settings[i].hour)
			document.getElementById('Settings').rows[i+1].cells.namedItem("hour").childNodes[0].value = response.settings[i].hour;
		if (response.settings[i].day)
			document.getElementById('Settings').rows[i+1].cells.namedItem("day").childNodes[0].value = response.settings[i].day;
		if (response.settings[i].month)
			document.getElementById('Settings').rows[i+1].cells.namedItem("month").childNodes[0].value = response.settings[i].month;
	}
}

function get_schdl_event_settings() {
	get_settings('/settings/events/schdl', parse_schdl_event_settings);
}

function set_schdl_event_settings() {
	var settings = {
		Settings:[]
	};
	for ( i = 0; i < document.getElementById("Settings").rows.length - 1; i++ )
	{
		if (document.getElementById('Settings').rows[i+1].cells.namedItem("id").childNodes[0].value != "")
		{			
			var setting = { 					
				id: parseInt(document.getElementById('Settings').rows[i+1].cells.namedItem("id").childNodes[0].value),				
			}
			if (document.getElementById('Settings').rows[i+1].cells.namedItem("min").childNodes[0].value != "") 
				setting["min"] = parseInt(document.getElementById('Settings').rows[i+1].cells.namedItem("min").childNodes[0].value)
			if (document.getElementById('Settings').rows[i+1].cells.namedItem("hour").childNodes[0].value != "") 
				setting["hour"] = parseInt(document.getElementById('Settings').rows[i+1].cells.namedItem("hour").childNodes[0].value)					
			if (document.getElementById('Settings').rows[i+1].cells.namedItem("day").childNodes[0].value != "") 
				setting["day"] = parseInt(document.getElementById('Settings').rows[i+1].cells.namedItem("day").childNodes[0].value)
			if (document.getElementById('Settings').rows[i+1].cells.namedItem("month").childNodes[0].value != "") 
				setting["month"] = parseInt(document.getElementById('Settings').rows[i+1].cells.namedItem("month").childNodes[0].value)
			settings.Settings.push(setting);
		}
	}
	set_settings('/settings/events/schdl',settings,'PUT');
};

function del_schdl_event_settings() {
	del_settings('/settings/events/schdl');
};

function parse_meter_action_settings(response) {                
	for (var i = 0; i < response.Settings.length; i++) {
		add_meter_action_row();
		document.getElementById('Settings').rows[i+1].cells.namedItem("id").childNodes[0].value = response.Settings[i].id;
		if (response.Settings[i].metersName)
			document.getElementById('Settings').rows[i+1].cells.namedItem("metersName").childNodes[0].value = response.Settings[i].metersName;
		document.getElementById('Settings').rows[i+1].cells.namedItem("archTypesName").childNodes[0].value = response.Settings[i].archTypesName;
	}
}

function get_meter_action_settings() {
	get_settings('/settings/actions/meter', parse_meter_action_settings);
}

function set_meter_action_settings() {
	var settings = {
		Settings:[]
	};
	for ( i = 0; i < document.getElementById("Settings").rows.length - 1; i++ )
	{
		if (document.getElementById('Settings').rows[i+1].cells.namedItem("id").childNodes[0].value != "")
		{			
			var setting = { 					
					id: parseInt(document.getElementById('Settings').rows[i+1].cells.namedItem("id").childNodes[0].value), 
					archTypesName: document.getElementById('Settings').rows[i+1].cells.namedItem("archTypesName").childNodes[0].value,
				}
			if (document.getElementById('Settings').rows[i+1].cells.namedItem("metersName").childNodes[0].value != "") 
				setting["metersName"] = document.getElementById('Settings').rows[i+1].cells.namedItem("metersName").childNodes[0].value
			settings.Settings.push(setting);
		}
	}
	set_settings('/settings/actions/meter',settings,'PUT');
};

function del_meter_action_settings() {
	del_settings('/settings/actions/meter');
};

function parse_sntp_action_settings(response) {                
	for (var i = 0; i < response.Settings.length; i++) {
		add_sntp_action_row();
		document.getElementById('Settings').rows[i+1].cells.namedItem("id").childNodes[0].value = response.Settings[i].id;
		document.getElementById('Settings').rows[i+1].cells.namedItem("eventType").childNodes[0].value = response.Settings[i].eventType;
		document.getElementById('Settings').rows[i+1].cells.namedItem("eventId").childNodes[0].value = response.Settings[i].eventId;	
	}
}

function get_sntp_action_settings() {
	get_settings('/settings/actions/sntp', parse_sntp_action_settings);
}

function set_sntp_action_settings() {
	var settings = {
		Settings:[]
	};
	for ( i = 0; i < document.getElementById("Settings").rows.length - 1; i++ )
	{
		if (document.getElementById('Settings').rows[i+1].cells.namedItem("id").childNodes[0].value != "")
		{			
			var setting = { 					
					id: parseInt(document.getElementById('Settings').rows[i+1].cells.namedItem("id").childNodes[0].value), 
					eventType: parseInt(document.getElementById('Settings').rows[i+1].cells.namedItem("eventType").childNodes[0].value),
					eventId: parseInt(document.getElementById('Settings').rows[i+1].cells.namedItem("eventId").childNodes[0].value),					
				}
			settings.Settings.push(setting);
		}
	}
	set_settings('/settings/actions/sntp',settings,'PUT');
};

function del_sntp_action_settings() {
	del_settings('/settings/actions/sntp');
};

function parse_event_manager_settings(response) {                
	for (var i = 0; i < response.Settings.length; i++) {
		add_event_manager_row();
		document.getElementById('Settings').rows[i+1].cells.namedItem("id").childNodes[0].value = response.Settings[i].id;
		document.getElementById('Settings').rows[i+1].cells.namedItem("eventType").childNodes[0].value = response.Settings[i].eventType;
		document.getElementById('Settings').rows[i+1].cells.namedItem("eventId").childNodes[0].value = response.Settings[i].eventId;
		document.getElementById('Settings').rows[i+1].cells.namedItem("actionType").childNodes[0].value = response.Settings[i].actionType;
		document.getElementById('Settings').rows[i+1].cells.namedItem("actionId").childNodes[0].value = response.Settings[i].actionId;		
	}
}

function get_event_manager_settings() {
	get_settings('/settings/events/manager', parse_event_manager_settings);
}

function set_event_manager_settings() {
	var settings = {
		Settings:[]
	};
	for ( i = 0; i < document.getElementById("Settings").rows.length - 1; i++ )
	{
		if (document.getElementById('Settings').rows[i+1].cells.namedItem("id").childNodes[0].value != "")
		{			
			var setting = { 					
					id: parseInt(document.getElementById('Settings').rows[i+1].cells.namedItem("id").childNodes[0].value), 
					eventType: document.getElementById('Settings').rows[i+1].cells.namedItem("eventType").childNodes[0].value,
					eventId: parseInt(document.getElementById('Settings').rows[i+1].cells.namedItem("eventId").childNodes[0].value),					
					actionType: document.getElementById('Settings').rows[i+1].cells.namedItem("actionType").childNodes[0].value,
					actionId: parseInt(document.getElementById('Settings').rows[i+1].cells.namedItem("actionId").childNodes[0].value),
				}
			settings.Settings.push(setting);
		}
	}
	set_settings('/settings/events/manager',settings,'PUT');
};

function del_event_manager_settings() {
	del_settings('/settings/events/manager');
};

function set_meter_time() {  
	var params = {
		id: parseInt(document.getElementById('Settings').rows[0].cells[1].childNodes[0].value)
	};
	set_settings('/meter/settings/time',params,'PUT');
}

function set_meter_relay_state() {  
	var params = {
		id: parseInt(document.getElementById('Settings').rows[0].cells[1].childNodes[0].value),
		relayId: parseInt(document.getElementById('Settings').rows[1].cells[1].childNodes[0].value),
		relayState: parseInt(document.getElementById('Settings').rows[2].cells[1].childNodes[0].value),
	};
	set_settings('/meter/settings/relay',params,'PUT');
}

function get_charge_process_state() {  
	var params = {
		ids:[],
		time:[],
		measure: "chargeProcessParams"
	};
	ID_search(params);
	time_search(params);
    var request = new XMLHttpRequest();
    request.open('POST', 'charge/data/arch');
	request.setRequestHeader('X-Protocol-USPD', '40');
	state_table_clear();
    request.onreadystatechange = function() {
        if (this.readyState == 4) {
            if ( this.status == 200) {
				charge_process_state_response_parse(JSON.parse(this.responseText));
            }
			if (this.status == 403)
			{
				redirect_to_home_page();
			}
        }
    }
    request.send(JSON.stringify(params));
}

function charge_process_state_response_parse(response) {
	var idx = 1;
	for (var i = 0; i < response.measures.length; i++) {
	    if ( response.measures[i].measure != "chargeProcessParams" )
			continue;
		for (var j = 0; j < response.measures[i].values.length; j++) {			
			add_charge_process_state_row();
			document.getElementById('State').rows[idx].cells.namedItem("stationTableId").childNodes[0].value = response.measures[i].values[j].stationTableId;
			document.getElementById('State').rows[idx].cells.namedItem("time").childNodes[0].value = response.measures[i].values[j].time;
			document.getElementById('State').rows[idx].cells.namedItem("sessionId").childNodes[0].value = response.measures[i].values[j].sessionId;
			document.getElementById('State').rows[idx].cells.namedItem("stationId").childNodes[0].value = response.measures[i].values[j].stationId;
			document.getElementById('State').rows[idx].cells.namedItem("chargeLevel").childNodes[0].value = response.measures[i].values[j].chargeLevel;
			idx++;
		}
	}
}

function get_charge_session_state() {  
	var params = {
		ids:[],
		time:[],
		measure: "chargeSessionParams"
	};
	ID_search(params);
	time_search(params);
    var request = new XMLHttpRequest();
    request.open('POST', 'charge/data/arch');
	request.setRequestHeader('X-Protocol-USPD', '40');
	state_table_clear();
    request.onreadystatechange = function() {
        if (this.readyState == 4) {
            if ( this.status == 200) {
				charge_session_state_response_parse(JSON.parse(this.responseText));
            }
			if (this.status == 403)
			{
				redirect_to_home_page();
			}
        }
    }
    request.send(JSON.stringify(params));
}

function charge_session_state_response_parse(response) {
	var idx = 1;
	for (var i = 0; i < response.measures.length; i++) {
	    if ( response.measures[i].measure != "chargeSessionParams" )
			continue;
		for (var j = 0; j < response.measures[i].values.length; j++) {			
			add_charge_session_state_row();
			document.getElementById('State').rows[idx].cells.namedItem("stationTableId").childNodes[0].value = response.measures[i].values[j].stationTableId;
			document.getElementById('State').rows[idx].cells.namedItem("stationId").childNodes[0].value = response.measures[i].values[j].stationId;
			document.getElementById('State').rows[idx].cells.namedItem("time").childNodes[0].value = response.measures[i].values[j].time;
			document.getElementById('State').rows[idx].cells.namedItem("sessionId").childNodes[0].value = response.measures[i].values[j].sessionId;
			document.getElementById('State').rows[idx].cells.namedItem("sessionStatus").childNodes[0].value = response.measures[i].values[j].sessionStatus;
			document.getElementById('State').rows[idx].cells.namedItem("stockId").childNodes[0].value = response.measures[i].values[j].stockId;
			document.getElementById('State').rows[idx].cells.namedItem("stockGarageId").childNodes[0].value = response.measures[i].values[j].stockGarageId;
			document.getElementById('State').rows[idx].cells.namedItem("p").childNodes[0].value = response.measures[i].values[j].p;
			document.getElementById('State').rows[idx].cells.namedItem("i").childNodes[0].value = response.measures[i].values[j].i;
			document.getElementById('State').rows[idx].cells.namedItem("u").childNodes[0].value = response.measures[i].values[j].u;
			document.getElementById('State').rows[idx].cells.namedItem("pSumm").childNodes[0].value = response.measures[i].values[j].pSumm;
			document.getElementById('State').rows[idx].cells.namedItem("startTime").childNodes[0].value = response.measures[i].values[j].startTime;
			document.getElementById('State').rows[idx].cells.namedItem("endTime").childNodes[0].value = response.measures[i].values[j].endTime;
			document.getElementById('State').rows[idx].cells.namedItem("startChargeLevel").childNodes[0].value = response.measures[i].values[j].startChargeLevel;
			document.getElementById('State').rows[idx].cells.namedItem("endChargeLevel").childNodes[0].value = response.measures[i].values[j].endChargeLevel;
			idx++;
		}
	}
}

function get_charge_station_state() {  
	var params = {
		ids:[],
		time:[],
		measure: "stationParams"
	};
	ID_search(params);
	time_search(params);
    var request = new XMLHttpRequest();
    request.open('POST', 'charge/data/arch');
	request.setRequestHeader('X-Protocol-USPD', '40');
	state_table_clear();
    request.onreadystatechange = function() {
        if (this.readyState == 4) {
            if ( this.status == 200) {
				charge_station_state_response_parse(JSON.parse(this.responseText));
            }
			if (this.status == 403)
			{
				redirect_to_home_page();
			}
        }
    }
    request.send(JSON.stringify(params));
}

function charge_station_state_response_parse(response) {
	var idx = 1;
	for (var i = 0; i < response.measures.length; i++) {
	    if ( response.measures[i].measure != "stationParams" )
			continue;
		for (var j = 0; j < response.measures[i].values.length; j++) {			
			add_charge_station_state_row();
			document.getElementById('State').rows[idx].cells.namedItem("stationTableId").childNodes[0].value = response.measures[i].values[j].stationTableId;
			document.getElementById('State').rows[idx].cells.namedItem("stationId").childNodes[0].value = response.measures[i].values[j].stationId;
			document.getElementById('State').rows[idx].cells.namedItem("time").childNodes[0].value = response.measures[i].values[j].time;
			document.getElementById('State').rows[idx].cells.namedItem("status").childNodes[0].value = response.measures[i].values[j].status;
			document.getElementById('State').rows[idx].cells.namedItem("p").childNodes[0].value = response.measures[i].values[j].p;
			document.getElementById('State').rows[idx].cells.namedItem("i").childNodes[0].value = response.measures[i].values[j].i;
			document.getElementById('State').rows[idx].cells.namedItem("u").childNodes[0].value = response.measures[i].values[j].u;
			document.getElementById('State').rows[idx].cells.namedItem("uIn").childNodes[0].value = response.measures[i].values[j].uIn;
			document.getElementById('State').rows[idx].cells.namedItem("temp").childNodes[0].value = response.measures[i].values[j].temp;
			document.getElementById('State').rows[idx].cells.namedItem("ap").childNodes[0].value = response.measures[i].values[j].ap;
			document.getElementById('State').rows[idx].cells.namedItem("apDay").childNodes[0].value = response.measures[i].values[j].apDay;
			document.getElementById('State').rows[idx].cells.namedItem("errors").childNodes[0].value = response.measures[i].values[j].errors;
			document.getElementById('State').rows[idx].cells.namedItem("errNoVoltage").childNodes[0].checked = response.measures[i].values[j].errNoVoltage;
			document.getElementById('State').rows[idx].cells.namedItem("errLowVoltage").childNodes[0].checked = response.measures[i].values[j].errLowVoltage;
			document.getElementById('State').rows[idx].cells.namedItem("errOverVoltage").childNodes[0].checked = response.measures[i].values[j].errOverVoltage;
			document.getElementById('State').rows[idx].cells.namedItem("errInsulationIn").childNodes[0].checked = response.measures[i].values[j].errInsulationIn;
			document.getElementById('State').rows[idx].cells.namedItem("errPowerOff").childNodes[0].checked = response.measures[i].values[j].errPowerOff;
			document.getElementById('State').rows[idx].cells.namedItem("errOverTemperature").childNodes[0].checked = response.measures[i].values[j].errOverTemperature;
			document.getElementById('State').rows[idx].cells.namedItem("errOpen").childNodes[0].checked = response.measures[i].values[j].errOpen;
			document.getElementById('State').rows[idx].cells.namedItem("errOverCurrent").childNodes[0].checked = response.measures[i].values[j].errOverCurrent;
			document.getElementById('State').rows[idx].cells.namedItem("errInsulationOut").childNodes[0].checked = response.measures[i].values[j].errInsulationOut;
			document.getElementById('State').rows[idx].cells.namedItem("errFireAlarm").childNodes[0].checked = response.measures[i].values[j].errFireAlarm;
			idx++;
		}
	}
}

function render_firmware_update_log() {
	get_settings('/upload/firmware', parse_firmware_update_log);
}

function parse_firmware_update_log(response) {
	const container = document.getElementById('FirmwareUpdateLog');
	for (let i = 0; i < response.Log.length; i++) {
		const paragraph = document.createElement('p');
		paragraph.innerHTML = response.Log[i];
		container.appendChild(paragraph);
	}
}

function fetch_text_settings(uri, parser) {
	const request = new XMLHttpRequest();
	request.open('GET', uri);
	request.setRequestHeader('X-Protocol-USPD', '40');
	request.onreadystatechange = function() {
		if (this.readyState == 4) {
			if (this.status == 200) {
				parser(this.responseText);
			}
			if (this.status == 403)
			{
				redirect_to_home_page();
			}
		}
	}
	request.send(null);
}

function render_firmware_update_detailed_log() {
	fetch_text_settings('/download/fwupdatelog', function(response) {
		const link = document.getElementById('FirmwareUpdateLogArchive');
		if (link && response) {
			link.setAttribute('href', response);
		}
	});
}

function upload_firmware(data, progress_callback) {
	const formElement = document.getElementById('FirmwareUpdateForm');
	const request = new XMLHttpRequest();
	request.open('POST', '/upload/firmware');
	request.setRequestHeader('X-Protocol-USPD', '40');
	request.withCredentials = true;
	request.upload.addEventListener('progress', function (e) {
		if (progress_callback) {
			const percent_completed = Math.floor(e.loaded / e.total * 100);
			progress_callback(percent_completed);
		}
	});
	request.addEventListener('readystatechange', function () {
		if (request.readyState === 4) {
			switch (request.status) {
				case 200:
					render_upload_result('200 OK, Update started, please wait until device reboots...');
					render_countdown_message(formElement, 120, 'Идет перезагрузка, осталось подождать', 'Перезагрузка завершена', redirect_to_home_page);
					break;
				case 403:
					redirect_to_home_page();
					break;
				default:
					render_upload_result('500 BAD, An error occured...');
					break;
			}
		}
	});
	request.send(data);
}

function render_upload_result(text) {
	const resultElement = document.getElementById('FirmwareUpdateResult');
	resultElement.innerHTML = text;
}

function render_upload_progress(progress_percent) {
	const progressElement = document.getElementById('FirmwareUploadProgress');
	progressElement.innerText = progress_percent + '%';
}

function handle_firmware_form_submit() {
	const formElement = document.getElementById('FirmwareUpdateForm');
	formElement.addEventListener('submit', function (event) {
		event.preventDefault();
		const formData = new FormData(event.target);
		upload_firmware(formData, render_upload_progress);
	});
}

function handle_restart_form_submit() {
	const formElement = document.getElementById('ActionRestartForm');
	formElement.addEventListener('submit', function (event) {
		event.preventDefault();
		restart_device();
		render_countdown_message(formElement, 120, 'Идет перезагрузка, осталось подождать', 'Перезагрузка завершена, обновите страницу в браузере');
	});
}

function restart_device() {
	const request = new XMLHttpRequest();
	request.open('POST', '/action/restart');
	request.setRequestHeader('X-Protocol-USPD', '40');
	request.withCredentials = true;
	request.addEventListener('readystatechange', function () {
		if (request.readyState === 4) {
			switch (request.status) {
				case 200:
				case 403:
					redirect_to_home_page();
					break;
				default:
					console.log(request);
					break;
			}
		}
	});
	request.send();
}

function render_countdown_message(parent, duration, progressText, successText, afterCallback) {
	const messageElement = document.createElement('div');
	parent.appendChild(messageElement);
	let timer = duration;
	const timerInterval = setInterval(function () {
		const minutes = Math.floor(timer / 60);
		const seconds = timer % 60;
		const displayMinutes = minutes < 10 ? `0${minutes}` : minutes;
		const displaySeconds = seconds < 10 ? `0${seconds}` : seconds;
		messageElement.innerHTML = `${progressText} ${displayMinutes}:${displaySeconds}`;
		if (--timer < 0) {
			clearInterval(timerInterval);
			messageElement.innerHTML = successText;
			if (afterCallback) {
				afterCallback();
			}
		}
	}, 1000);
}
