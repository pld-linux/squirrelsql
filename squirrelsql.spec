Summary:	SQL database manager
Summary(pl):	Zarz±dca SQL-owych baz danych
Name:		squirrelsql
Version:	1.0final2
Release:	1
License:	GPL
Group:		Applications/Databases/Interfaces
Source0:	http://dl.sourceforge.net/squirrel-sql/squirrel-sql-%{version}.tar.gz
# Source0-md5:	ae31f24db8fa27f85994bb676b79b1c7
Source1:	squirrelsql.desktop
URL:		http://squirrel-sql.sourceforge.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SQuirreL SQL Client is a graphical Java program that will allow you to
view the structure of a JDBC compliant database, browse the data in
tables, issue SQL commands etc.

%description -l pl
Klient SQL SQuirreL jest graficznym programem napisanym w Javie, który
pozwala przegl±daæ strukturê baz danych zgodnych z JDBC, przegl±daæ
dane w tabelach, wysy³aæ polecenia SQL-owe itp.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/opt/%{name}-%{version},%{_bindir},%{_applnkdir}/Utilities}
cd $RPM_BUILD_ROOT/opt/%{name}-%{version}
tar xfz %{SOURCE0}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Utilities

cat << EOF > $RPM_BUILD_ROOT%{_bindir}/squirrelsql
#!/bin/sh
cd /opt/%{name}-%{version}
exec ./squirrel-sql.sh
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir /opt/%{name}-%{version}
%attr(755,root,root) /opt/%{name}-%{version}/*.sh
/opt/%{name}-%{version}/*.jar
/opt/%{name}-%{version}/[dlp]*
%{_applnkdir}/Utilities/*
