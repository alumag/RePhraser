<%@ Page Title="" Language="C#" MasterPageFile="~/master.Master" AutoEventWireup="true" CodeBehind="rephrase.aspx.cs" Inherits="Website.rephrase" EnableEventValidation="false"%>

<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="ContentPlaceHolder1" runat="server">
    <form id="form1">
        <div class="form_settings">
            <h3>File To Rephrase:</h3>
            <br />
            <asp:FileUpload ID="FileUpload1" accept=".txt" runat="server" />
            <br />
            <br />
            <asp:Button ID="btnsave" runat="server" OnClick="btnsave_Click" Text="Do the magic" Style="width: 85px" />
            <br />
            <br />
            <asp:Label ID="lblmessage" runat="server" />
        </div>

    </form>
</asp:Content>
