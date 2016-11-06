/* start module: test */
$pyjs['loaded_modules']['test'] = function (__mod_name__) {
	if($pyjs['loaded_modules']['test']['__was_initialized__']) return $pyjs['loaded_modules']['test'];
	var $m = $pyjs['loaded_modules']['test'];
	$m['__repr__'] = function() { return '<module: test>'; };
	$m['__was_initialized__'] = true;
	if ((__mod_name__ === null) || (typeof __mod_name__ == 'undefined')) __mod_name__ = 'test';
	$m['__name__'] = __mod_name__;


	$m['pyjd'] = $p['___import___']('pyjd', null);
	$m['RootPanel'] = $p['___import___']('pyjamas.ui.RootPanel.RootPanel', null, null, false);
	$m['Button'] = $p['___import___']('pyjamas.ui.Button.Button', null, null, false);
	$m['Label'] = $p['___import___']('pyjamas.ui.Label.Label', null, null, false);
	$m['Window'] = $p['___import___']('pyjamas.Window', null, null, false);
	$m['Grid'] = $p['___import___']('pyjamas.ui.Grid.Grid', null, null, false);
	$m['Hyperlink'] = $p['___import___']('pyjamas.ui.Hyperlink.Hyperlink', null, null, false);
	$m['TextBox'] = $p['___import___']('pyjamas.ui.TextBox.TextBox', null, null, false);
	$m['RegisterWidget'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition['__module__'] = 'test';
		$method = $pyjs__bind_method2('__init__', function() {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}

			self['registerService'] = (typeof RegisterService == "undefined"?$m['RegisterService']:RegisterService)(self);
			self['nameField'] = $m['TextBox']();
			self['passwordField'] = $m['TextBox']();
			self['passwordConfirmField'] = $m['TextBox']();
			self['emailField'] = $m['TextBox']();
			self['ssnField'] = $m['TextBox']();
			self['phoneField'] = $m['TextBox']();
			self['zipCodeField'] = $m['TextBox']();
			self['addressField'] = $m['TextBox']();
			self['statusLabel'] = $m['Label']();
			self['registerButton'] = $m['Button']();
			self['buildForm']();
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['__init__'] = $method;
		$method = $pyjs__bind_method2('buildForm', function() {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var formGrid;
			formGrid = $m['Grid'](2, 10);
			formGrid['setVisible'](false);
			formGrid['setWidget'](1, 0, $p['getattr'](self, 'statusLabel'));
			formGrid['setWidget'](0, 1, $m['Label']('Name: '));
			formGrid['setWidget'](1, 1, $p['getattr'](self, 'nameField'));
			formGrid['setWidget'](0, 2, $m['Label']('Password: '));
			formGrid['setWidget'](1, 2, $p['getattr'](self, 'passwordField'));
			formGrid['setWidget'](0, 3, $m['Label']('Password: '));
			formGrid['setWidget'](1, 3, $p['getattr'](self, 'passwordConfirmField'));
			formGrid['setWidget'](0, 4, $m['Label']('E-mail: '));
			formGrid['setWidget'](1, 4, $p['getattr'](self, 'emailField'));
			formGrid['setWidget'](0, 5, $m['Label']('SSN: '));
			formGrid['setWidget'](1, 5, $p['getattr'](self, 'ssnField'));
			formGrid['setWidget'](0, 6, $m['Label']('Phone: '));
			formGrid['setWidget'](1, 6, $p['getattr'](self, 'phoneField'));
			formGrid['setWidget'](0, 7, $m['Label']('Address: '));
			formGrid['setWidget'](1, 7, $p['getattr'](self, 'addressField'));
			formGrid['setWidget'](0, 8, $m['Label']('Zip Code: '));
			formGrid['setWidget'](1, 8, $p['getattr'](self, 'zipCodeField'));
			self['formGrid'] = formGrid;
			$m['RootPanel']('RegisterWidget')['add'](formGrid);
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['buildForm'] = $method;
		var $bases = new Array(pyjslib['object']);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data['__setitem__']($item, $cls_definition[$item]); }
		return $p['_create_class']('RegisterWidget', $p['tuple']($bases), $data);
	})();
	$m['User'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition['__module__'] = 'test';
		$method = $pyjs__bind_method2('__init__', function(name, ssn, address, email, zipCode, phone, password) {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
				name = arguments[1];
				ssn = arguments[2];
				address = arguments[3];
				email = arguments[4];
				zipCode = arguments[5];
				phone = arguments[6];
				password = arguments[7];
			}
			if (typeof name == 'undefined') name=arguments['callee']['__args__'][3][1];
			if (typeof ssn == 'undefined') ssn=arguments['callee']['__args__'][4][1];
			if (typeof address == 'undefined') address=arguments['callee']['__args__'][5][1];
			if (typeof email == 'undefined') email=arguments['callee']['__args__'][6][1];
			if (typeof zipCode == 'undefined') zipCode=arguments['callee']['__args__'][7][1];
			if (typeof phone == 'undefined') phone=arguments['callee']['__args__'][8][1];
			if (typeof password == 'undefined') password=arguments['callee']['__args__'][9][1];

			self['$$name'] = name;
			self['ssn'] = (typeof snn == "undefined"?$m['snn']:snn);
			self['address'] = address;
			self['email'] = email;
			self['zipCode'] = zipCode;
			self['phone'] = phone;
			self['password'] = password;
			return null;
		}
	, 1, [null,null,['self'],['name', ''],['ssn', ''],['address', ''],['email', ''],['zipCode', ''],['phone', ''],['password', '']]);
		$cls_definition['__init__'] = $method;
		var $bases = new Array(pyjslib['object']);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data['__setitem__']($item, $cls_definition[$item]); }
		return $p['_create_class']('User', $p['tuple']($bases), $data);
	})();
	$m['RegisterService'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition['__module__'] = 'test';
		$method = $pyjs__bind_method2('__init__', function(callback) {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
				callback = arguments[1];
			}

			self['callback'] = callback;
			return null;
		}
	, 1, [null,null,['self'],['callback']]);
		$cls_definition['__init__'] = $method;
		$method = $pyjs__bind_method2('addUser', function(user) {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
				user = arguments[1];
			}

			self['callback']['service_eventAddUserSuccessful']();
			return null;
		}
	, 1, [null,null,['self'],['user']]);
		$cls_definition['addUser'] = $method;
		$method = $pyjs__bind_method2('updateUser', function(user) {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
				user = arguments[1];
			}

			self['callback']['service_eventUpdateUserSuccessful']();
			return null;
		}
	, 1, [null,null,['self'],['user']]);
		$cls_definition['updateUser'] = $method;
		$method = $pyjs__bind_method2('removeUser', function(user) {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
				user = arguments[1];
			}

			self['callback']['service_eventRemoveUserSuccessful']();
			return null;
		}
	, 1, [null,null,['self'],['user']]);
		$cls_definition['removeUser'] = $method;
		var $bases = new Array(pyjslib['object']);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data['__setitem__']($item, $cls_definition[$item]); }
		return $p['_create_class']('RegisterService', $p['tuple']($bases), $data);
	})();
	if ($p['bool']($p['op_eq']((typeof __name__ == "undefined"?$m['__name__']:__name__), (typeof __main__ == "undefined"?$m['__main__']:__main__)))) {
		$m['pyjd']['setup']('templates/register.html');
	}
	return this;
}; /* end test */


/* end module: test */


/*
PYJS_DEPS: ['pyjd', 'pyjamas.ui.RootPanel.RootPanel', 'pyjamas', 'pyjamas.ui', 'pyjamas.ui.RootPanel', 'pyjamas.ui.Button.Button', 'pyjamas.ui.Button', 'pyjamas.ui.Label.Label', 'pyjamas.ui.Label', 'pyjamas.Window', 'pyjamas.ui.Grid.Grid', 'pyjamas.ui.Grid', 'pyjamas.ui.Hyperlink.Hyperlink', 'pyjamas.ui.Hyperlink', 'pyjamas.ui.TextBox.TextBox', 'pyjamas.ui.TextBox']
*/
