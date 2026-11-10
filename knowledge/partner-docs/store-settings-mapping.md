---
# Synced from https://docs.zid.sa/store-settings-mapping-1379317m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-store-settings-mapping
title: "Store Settings Mapping"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/store-settings-mapping-1379317m0
tags: [from-docs-site, partner-docs]
language: en
---

> Store Settings Mapping - Zid Docs
# Store Settings Mapping

This guide will help you migrate **store settings** from the old system to the new **Vitrin** theme structure. All **global store settings** are now available under the `settings` object inside the `store` object. The structure is reorganized and grouped into **logical categories** for easier access and maintenance.

Use this mapping to update your theme code and ensure settings are referenced from their **new paths**.

## 🎨 Branding #

Brand-related settings (logo, colors, description, etc.) are now grouped under `branding`.

Type **New Path** Old Path

`string[url]` `store.settings.branding.logo` `store.logo`

`string[url]` `store.settings.branding.icon` `store.icon`

`string[url]` `store.settings.branding.cover` `store.cover`

`string` `store.settings.branding.description` `store.description`

`string` `store.settings.branding.copyrights` `store.copyrights`

`string[hex]` `store.settings.branding.colors.primary` `store.colors.primary`

`string[hex]` `store.settings.branding.colors.on_primary` `store.colors.text_of_primary_bg`

`string[hex]` `store.settings.branding.colors.primary_variant` `store.colors.primary`

`string[hex]` `store.settings.branding.colors.secondary` `store.colors.primary`

`string[hex]` `store.settings.branding.colors.on_secondary` `store.colors.text_of_primary_bg`

`string[hex]` `store.settings.branding.colors.secondary_variant` `store.colors.primary`

`string` `store.settings.general.one_signal.ios_app_id` `store.apps.ios_app_id`

`string` `store.settings.general.one_signal.android_package_name` `store.apps.android_package_name`

## ⚙ General Settings #

General store configuration such as currency, tax settings, availability, and app tabs.

New Path Old Path Type

`store.settings.general.currency.*` `store.currency` `Currency`

`store.settings.general.business_address` `store.business_location`

`store.settings.general.tax_settings.*` `store.vat_settings` `TaxSettings`

`store.settings.general.availability.*` `store.availability` `Availability`

`store.settings.general.mobile_app_tab.*` `store.mobile_app_tab_settings`

`store.settings.general.mazeed.display_places.customer_profile_page` `store.mazeed_display_places.customer_profile_page` `boolean`

`store.settings.general.mazeed.display_places.order_success_page` `store.mazeed_display_places.order_success_page` `boolean`

`store.settings.general.mazeed.display_places.order_view_page` `store.mazeed_display_places.order_view_page` `boolean`

### Currency #

Handles currency format, display, and exchange rates.

New Path Old Path Type

`store.settings.general.currency.id` `store.currency.id` `int`

`store.settings.general.currency.name` `store.currency.name` `string`

`store.settings.general.currency.code` `store.currency.code` `string`

`store.settings.general.currency.symbol` `store.currency.symbol` `string`

`store.currency.country`

`store.settings.general.currency.symbol_left` `string`

`store.settings.general.currency.symbol_right` `string`

`store.settings.general.currency.format` `string`

`store.settings.general.currency.exchange_rate` `string`

### Tax Settings #

VAT & tax-related settings.

New Path Old Path Type

`store.settings.general.tax_settings.id` `store.vat_settings.id` `uuid`

`store.settings.general.tax_settings.country` `string`

`store.settings.general.tax_settings.tax_percentage` `store.vat_settings.tax_percentage` `float`

`store.settings.general.tax_settings.tax_number` `store.vat_settings.vat_number` `string`

`store.settings.general.tax_settings.tax_registration_certificate` `store.vat_settings.tax_registration_certificate` `string[url]`

`store.settings.general.tax_settings.is_certificate_visible` `store.vat_settings.is_certificate_visible` `boolean`

`store.settings.general.tax_settings.is_tax_number_visible` `store.vat_settings.is_vat_number_visible` `boolean`

`store.settings.general.tax_settings.tax_activate` `store.vat_settings.vat_activate` `boolean`

`store.settings.general.tax_settings.is_tax_self_paid` `store.vat_settings.is_vat_self_paid` `boolean`

`store.settings.general.tax_settings.is_tax_included_in_product_price` `store.vat_settings.is_vat_included_in_product_price` `boolean`

`store.settings.general.tax_settings.is_shipping_fee_included_in_tax` `store.vat_settings.is_shipping_fee_included_in_vat` `boolean`

`store.settings.general.tax_settings.can_use_tax` `store.vat_settings.can_use_vat` `boolean`

### Availability #

Store open/close settings, display messages, and timing.

Type New Path Old Path

`boolean` `store.settings.general.availability.is_store_closed` `store.availability.is_store_closed`

`string` `store.settings.general.availability.closing_type` `store.availability.closing_type`

`string` `store.settings.general.availability.closing_time_type` `store.availability.closing_time_type`

`boolean` `store.settings.general.availability.closed_now` `store.availability.closed_now`

`dict` `store.settings.general.availability.activating_data` `store.availability.activating_data`

`dict` `store.settings.general.availability.closing_data` `store.availability.closing_data`

`boolean` `store.settings.general.availability.notify_customer` `store.availability.notify_customer`

`boolean` `store.settings.general.availability.is_time_counter_displayed` `store.availability.is_time_counter_displayed`

`boolean` `store.settings.general.availability.is_available_hours_visible` `store.availability.is_available_hours_visible`

`string` `store.settings.general.availability.title` `store.availability.title`

`string` `store.settings.general.availability.message` `store.availability.message`

`string` `store.settings.general.availability.times` `store.availability.times`

## 📞 Contact Information #

Now consolidated under `contact`.

Type New Path Old Path

`string` `store.settings.contact.title` `store.social_media.title`

`string` `store.settings.contact.facebook` `store.social_media.items.facebook`

`string` `store.settings.contact.twitter` `store.social_media.items.twitter`

`string` `store.settings.contact.instagram` `store.social_media.items.instagram`

`string` `store.settings.contact.snapchat` `store.social_media.items.snapchat`

`string` `store.settings.contact.tiktok` `store.social_media.items.tiktok`

`string` `store.settings.contact.business_center` `store.social_media.items.business_center`

`string` `store.settings.contact.website` `store.social_media.items.website`

`string` `store.settings.contact.phone` `store.social_media.items.phone`

`string` `store.settings.contact.email` `store.social_media.items.email`

## 🏢 About Us #

This only applies if your theme was previously relying on the title and the text coming from the template settings. The new way uses the store settings object.

New Path Old Path Type

`store.settings.about_us.title` `store.about_us.title` `string`

`store.settings.about_us.text` `store.about_us.text` `string`

## 📢 Announcement Bar #

New Path Old Path

`store.settings.announcement_bar.*` `store.announcement_bar.*`

## 📋 Menus #

New Path Old Path

`store.settings.menus.main_menu.*` `store.menu_v2.*` ↳ Children remain in `items/children` same as before

## 📦 Products #

(low stock labels, wishlist, reviews, filters, payment widgets)

Type New Path Old Path

`boolean` `store.settings.products.low_stock_label_enabled` `store.is_low_stock_label_enabled`

`int/none` `store.settings.products.low_stock_quantity_limit` `store.low_stock_quantity_limit`

`boolean` `store.settings.products.wishlist_enabled` `store.is_wishlist_enabled`

`boolean` `store.settings.products.reviews_enabled` `store.is_product_reviews_enabled`

`boolean` `store.settings.products.questions_enabled` `store.is_product_question_and_answer_enabled`

`boolean` `store.settings.products.filter_by_city` `store.is_filter_products_based_on_city`

`boolean` `store.settings.products.tamara_widget_enabled` `store.is_tamara_product_widget_enabled`

`boolean` `store.settings.products.tabby_widget_enabled` `store.is_tabby_product_widget_enabled`

`boolean` `store.settings.products.has_products_filtration` `store.has_new_products_service`

`boolean` `store.settings.products.is_metafields_enabled` `store.is_metafields_enabled`

## 👤 Customers #

Type New Path Old Path

`boolean` `store.settings.customers.is_customers_email_mandatory` `store.is_customers_email_mandatory`

`boolean` `store.settings.customers.login_by_sms_enabled` `store.customers_login_by_sms_status`

`boolean` `store.settings.customers.login_by_email_enabled` `store.customers_login_by_email_status`

`boolean` `store.settings.customers.login_by_whatsapp_enabled` `store.customers_login_by_whatsapp_status`

`boolean` `store.settings.customers.gmaps_in_address_enabled` `store.is_gmaps_in_address_enabled`

`boolean` `store.settings.customers.gmaps_in_address_mandatory` `store.is_gmaps_in_address_mandatory`

`boolean` `store.settings.customers.spl_in_address_enabled` `store.is_spl_in_address_enabled`

`boolean` `store.settings.customers.gmaps_or_spl_enabled` `store.is_gmaps_and_spl_in_address_enabled`

`dict[string, any]` `store.settings.customers.google_maps` `store.google_maps`

## 💳 Checkout #

(payment options, widgets, restrictions, guest checkout, addresses)

Type New Path Old Path

`boolean` `store.settings.checkout.reorder_enabled` `store.is_reorder_enabled`

`boolean` `store.settings.checkout.is_selling_blocked` `store.is_selling_blocked`

`boolean` `store.settings.checkout.is_international_charge_notice_enabled` `store.is_international_charge_notice_enabled`

`boolean` `store.settings.checkout.show_pickup_option_stock_availability_for_checkout` `store.show_pickup_option_stock_availability_for_checkout`

`boolean` `store.settings.checkout.is_different_consignee_allowed` `store.is_different_consignee_allowed`

`string` `store.settings.checkout.tamara_public_key` `store.tamara_public_key`

`boolean` `store.settings.checkout.is_tamara_cart_widget_enabled` `store.is_tamara_cart_widget_enabled`

`list` `store.settings.checkout.payment_methods` `store.payment_methods`

`object` `store.settings.checkout.gift_order_settings` `store.gift_order_settings`

`boolean` `store.settings.checkout.is_coupon_form_enabled` `store.gift_order_settings`

## 📜 App Scripts #

Type New Path Old Path

`int` `store.settings.published_app_scripts[].id` `store.app_scripts[].script_id`

`string` `store.settings.published_app_scripts[].url` `store.app_scripts[].url`

`boolean` `store.settings.published_app_scripts[].status` `store.app_scripts[].status`

`int` `store.settings.published_app_scripts[].app_id` `store.app_scripts[].app_id`

`string` `store.settings.published_app_scripts[].version` `store.app_scripts[].version`

✅ **Next Step:** After updating your settings references, test your theme in a staging environment to confirm all features and visual elements render correctly.

Modified at 2026-08-04 09:49:50

Previous

Breaking Changes

Next

Architecture
