Summary:	SQL database manager
Summary(pl):	Mened¿er SQLowych baz danych
Name:		squirrelsql
Version:	1.0final2
Release:	1
License:	GPL
Group:		Applications/Databases/Interfaces
Source0:	http://twtelecom.dl.sourceforge.net/sourceforge/squirrel-sql/squirrel-sql-1.0final2.tar.gz
Source1:	squirrelsql.desktop
URL:		http://squirrel-sql.sourceforge.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
SQuirreL SQL Client is a graphical Java program that will allow you to
view the structure of a JDBC compliant database, browse the data in
tables, issue SQL commands etc.

%description -l pl
SQuirreL SQL CLient jest graficznym programem napisanym w Javie, który
pozwala przegl±daæ strukturê baz danych zgodnych z JDBC, przegl±daæ
dane w tabelach, wysy³aæ polecenia SQL-owe itp.

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/opt/%{name}-%{version},%{_bindir},%{_applnkdir}/Utilities}
cd $RPM_BUILD_ROOT/opt/%{name}-%{version}
tar xfz %{SOURCE0}

install %{SOURCE1} $RPM_BUILD_ROOT/%{_applnkdir}/Utilities

cat << EOF > $RPM_BUILD_ROOT%{_bindir}/squirrelsql
#!/bin/sh
cd /opt/%{name}-%{version}
exec ./squirrel-sql.sh
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /opt/%{name}-%{version}/*.sh
%attr(755,root,root) %{_bindir}/*
/opt/%{name}-%{version}/*.jar
/opt/%{name}-%{version}/[dlp]*
%{_applnkdir}/Utilities/*
