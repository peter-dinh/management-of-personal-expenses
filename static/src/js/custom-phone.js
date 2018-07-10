odoo.define('expenditure.custom_phone', function(require) {
    'use strict';


var FormRender = require('web.FormRenderer')
    
var core = require('web.core')
var field_registry = require('web.field_registry')
var InputField = require('web.basic_fields').InputField;


var CustomPhoneWidget = InputField.extend({
    init: function() {
        this._super.apply(this, arguments);
        console.log('this :', this);
    },
    
    _renderReadonly: function () {
        this._super.apply(this, arguments);
        this.$el.append("<a style='margin-left:10px;' href='tel:" + this.value + "'><span class='fa fa-phone'></span></a>")
        console.log("emo " + this.$el)
    }

});

FormRender.include({

    _renderTagLabel: function(node){
        var result = this._super.apply(this, arguments);
        if (node.attrs.icon == 'label_icon_phone'){
            console.log('Render Label');
            var result = this._super.apply(this, arguments);
            result.empty();
            result.append('<span class="fa fa-phone-square" style="font-size:10px;"></span>');
            return result;
        }
        return result;
    }
});

field_registry.add('custom_phone', CustomPhoneWidget);
});
