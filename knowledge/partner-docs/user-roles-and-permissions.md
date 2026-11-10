---
# Synced from https://docs.zid.sa/-user-roles-and-permissions-604944m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-user-roles-and-permissions
title: "📄 User Roles and Permissions"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/-user-roles-and-permissions-604944m0
tags: [from-docs-site, partner-docs]
language: en
---

> 📄 User Roles and Permissions - Zid Docs
# 📄 User Roles and Permissions

## Overview #

User roles and permissions determine what a user can view, change, or manage in a store's setting, i.e., from the Merchant Dashboard. User roles categorize users based on their level of access and responsibilities, whereas permissions provide fine-grained control over various functionalities within those roles. Together, they ensure that each user has access to the areas they need, without compromising the store's security or consistency.

## User Roles #

In our API, we categorize the users into two main roles: **`Customer`** and **`Manager`**. Each of these roles comes with different levels of access and permissions within the API.

### **Customer** #

A **`Customer`** is a role associated with end-users or shoppers in the system. Customers have the ability to perform actions related to shopping from the stores supported by Zid, such as browsing products, adding items to the shopping cart, and checking out.

When interacting with the API, set the **`Role`** header in the request to **`Customer`** to perform operations as a customer.

### **Manager** #

A **`Manager`** is a role associated with higher-level users who have the ability to manage different aspects of a store. This includes store owners, inventory managers, order managers, product managers, and other staff members.

**`Store Owner`**: Store owners have the highest level of access to a store, including creating, updating, and managing all aspects of their store. They also have the ability to create accounts for other store staff and assign them permissions.

**`Other Staff Members`**: Other staff members can have varying levels of access to the store based on the permissions granted to them by the store owner.

When interacting with the API, set the **`Role`** header in the request to **`Manager`** to perform operations as a store owner or other staff members.

**Note**: The Manager role in the API is an umbrella term for different roles within a store. The specific permissions assigned to each user within this category dictate the actions they can perform. The Manager term in the API documentation should be interpreted as Store Owner or Staff Member based on the context.

By setting the **`Role`** header in your request, you determine the level of access your request will have within the system. However, always keep in mind that each user's array of permissions ultimately dictates what actions they can perform.

## **List of Available Permissions** #

The following table provides details on all available permissions within our system. Each permission has a unique slug, along with descriptions in both English and Arabic, to ensure clarity and understanding.

Permission Slug English Description Arabic Description

`manage.store.marketing` Manage store marketing إدارة تسويق المتجر

`manage.app.market.details` Manage app market details / purchase subscription إدارة تفاصيل السوق / اشتراك الشراء

`manage.zidship.settings` Manage Zid Ship settings إدارة إعدادات زد شب

`manage.store.ecosystem.consultation` E-commerce consulting service خدمة الاستشارات في التجارة الإلكترونية

`manage.store.ecosystem.packaging` Manage packaging إدارة التغليف

`manage.store.vat.settings` Manage VAT settings إدارة إعدادات الضريبة

`manage.store.discount.rules` Manage automatic discounts إدارة الخصومات التلقائية

`pos.cashiers.page` Access cashier page الدخول إلى صفحة الكاشير

`manage.store.abandonedcarts` Manage abandoned carts إدارة السلات المتروكة

`manage.store.bundleoffers` Manage marketing bundles إدارة الحزم التسويقية

`manage.zidpay.setting` Manage Zid Pay settings إدارة إعدادات زدباي

`view.store.dashboard` View store dashboard عرض لوحة معلومات المتجر

`pos.cashier.usage` Use cashier for sales operations استخدام الكاشير لعمليات البيع

`manage.zidship.orders` Manage shipping orders إدارة أوامر الشحن

`pos.homepage` Access POS homepage الدخول إلى الصفحة الرئيسية لنقاط البيع

`list.store.customers` List store customers قائمة العملاء في المتجر

`manage.store.ecosystem.orderfulfillment` Manage orders and operations إدارة الطلبات والعمليات

`manage.app.market.settings` Manage application settings إدارة إعدادات التطبيق

`list.zidpay.transactions` List transactions قائمة العمليات

`manage.store.ecosystem.printings` Manage promotional printings إدارة المطبوعات الدعائية

`view.app.market.home` View app market homepage عرض الصفحة الرئيسية لسوق التطبيقات

`view.zidship.reports` View Zid Ship reports عرض تقارير زد شب

`manage.zid.financing` Manage Zid financing إدارة تمويل زد

`manage.store.front.customization` Customize store front تخصيص واجهة المتجر

`list.store.orders` List store orders قائمة طلبات المتجر

`manage.store.ecosystem.designs` Manage designs إدارة التصميمات

`manage.store.custom.domain` Manage custom domain إدارة النطاق المخصص

`manage.store.inventory.addresses` Manage inventory locations إدارة مواقع المخزون

`manage.store.ecosystem.payments` Manage payments إدارة الدفع

`manage.store.ecosystem.marketing` Manage marketing إدارة التسويق

`list.store.products` List all products قائمة جميع المنتجات

`manage.store.affiliate` Manage affiliate marketing إدارة التسويق بالعمولة

`list.store.categories` List product categories قائمة تصنيفات المنتجات

`view.zid.academy` View Zid Academy عرض أكاديمية زد

`manage.store.ecosystem.mobileapps` Mobile app service خدمة تطبيق الجوال

`manage.store.staff.notifications` Manage team notifications إدارة الإشعارات للفريق

`manage.store.settings` Manage store settings إدارة إعدادات المتجر

`manage.store.ecosystem.storepreparation` Store preparation service خدمة تجهيز المتجر

`refund.zidpay.transactions` Refund transactions استرداد المبالغ

`manage.zidship.payments` Manage service payments إدارة الدفع للخدمات

`pos.payment.methods` Manage payment methods إدارة طرق الدفع

`manage.store.ecosystem.delivery` Manage shipping and delivery إدارة الشحن والتوصيل

`manage.store.ecosystem.selfstorage` Manage self-storage units إدارة وحدات التخزين الذاتي

`manage.store.subscription` Manage subscriptions إدارة الاشتراكات

`list.zidpay.deposits` List account statement قائمة كشف الحساب

`pos.analytics` View POS reports عرض تقارير نقاط البيع

`view.store.home` View store homepage عرض الصفحة الرئيسية للمتجر

`create.store.orders` Create customer order إنشاء طلب للعميل

`list.store.order.drafts` List order drafts قائمة المسودات

`manage.store.ecosystem.photographics` Manage photography إدارة التصوير

`manage.store.account.settings` Manage account settings إدارة إعدادات الحساب

`manage.store.ecosystem.workplaces` Manage co-working spaces إدارة المساحات العمل المشتركة

`edit.store.orders` Edit customer order تعديل طلب العميل

`manage.store.zid.keys` Manage Zid keys إدارة مفاتيح زد

`manage.store.coupons` Manage discount coupons إدارة قسائم التخفيض

`view.app.market.browse` Browse app by category تصفح التطبيق حسب الفئة

`manage.store.front.pages` Manage additional pages إدارة الصفحات الإضافية

## **Understanding Permission Slugs** #

Permission slugs offer insights into the particular functionality they control in the store settings. They typically follow a **`manage.<entity>.<action>`** or **`view.<entity>`** or **`list.<entity>`** format.

**`manage`** signifies permissions that allow managing or modifying something.

**`view`** denotes permissions that allow viewing or accessing certain areas.

**`list`** is used for permissions that allow the user to see a list of specific entities.

**`<entity>`** refers to the specific area or feature the permission applies to, such as 'store.marketing' or 'store.inventory.addresses'.

**`<action>`** gives more detail about what the permission allows, for example, 'settings' or 'customization'.

## **Important Notes** #

Please note that all permissions are tied to the user's role in the system. Different roles have different sets of permissions, and not every role has access to every permission. This design ensures the security and consistency of your store's operations.

If you need any further clarification or have questions about specific permissions or roles, please contact our support team for assistance. We're here to help!

Modified at 2026-07-30 11:49:13

Previous

Store Settings

Next

Retrieve Store Manager Profile
