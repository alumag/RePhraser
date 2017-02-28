<%@ Page Title="" Language="C#" MasterPageFile="~/master.Master" AutoEventWireup="true" CodeBehind="contact.aspx.cs" Inherits="Website.contact" %>

<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="ContentPlaceHolder1" runat="server">
    <div id="content">
        <h1>Contact Us</h1>
        <form action="mailto:violetaluma@hotmail.com" method="post">
            <div class="form_settings">
                <p><span>Name</span><input class="contact" type="text" name="your_name" value="" /></p>
                <p><span>Email Address</span><input class="contact" type="text" name="your_email" value="" /></p>
                <p><span>Message</span><textarea class="contact textarea" rows="8" cols="50" name="your_enquiry"></textarea></p>
                <p style="padding-top: 15px"><span>&nbsp;</span><input class="submit" type="submit" name="contact_submitted" value="submit" /></p>
            </div>
        </form>
        <p>
            <br />
            <br />
            NOTE: A contact form such as this would require some way of emailing the input to an email address.</p>
    </div>
</asp:Content>
