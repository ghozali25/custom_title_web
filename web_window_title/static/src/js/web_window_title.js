odoo.define('custom_title_web', function (require) {
"use strict";

var AbstractWebClient = require('web.AbstractWebClient');
AbstractWebClient.include({
    init: function() {
        this._super.apply(this, arguments);
        this.set('title_part', {"zopenerp": document.title});
    }
});

});