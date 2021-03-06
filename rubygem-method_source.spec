#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-method_source
Version  : 0.8.2
Release  : 8
URL      : https://rubygems.org/downloads/method_source-0.8.2.gem
Source0  : https://rubygems.org/downloads/method_source-0.8.2.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-bacon
BuildRequires : rubygem-rdoc

%description
method_source
=============
(C) John Mair (banisterfiend) 2011
_retrieve the sourcecode for a method_

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n method_source-0.8.2
gem spec %{SOURCE0} -l --ruby > rubygem-method_source.gemspec

%build
gem build rubygem-method_source.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
method_source-0.8.2.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/method_source-0.8.2.gem
/usr/lib64/ruby/gems/2.3.0/gems/method_source-0.8.2/.gemtest
/usr/lib64/ruby/gems/2.3.0/gems/method_source-0.8.2/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/method_source-0.8.2/.yardopts
/usr/lib64/ruby/gems/2.3.0/gems/method_source-0.8.2/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/method_source-0.8.2/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/method_source-0.8.2/README.markdown
/usr/lib64/ruby/gems/2.3.0/gems/method_source-0.8.2/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/method_source-0.8.2/lib/method_source.rb
/usr/lib64/ruby/gems/2.3.0/gems/method_source-0.8.2/lib/method_source/code_helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/method_source-0.8.2/lib/method_source/source_location.rb
/usr/lib64/ruby/gems/2.3.0/gems/method_source-0.8.2/lib/method_source/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/method_source-0.8.2/method_source.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/method_source-0.8.2/test/test.rb
/usr/lib64/ruby/gems/2.3.0/gems/method_source-0.8.2/test/test_code_helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/method_source-0.8.2/test/test_helper.rb
/usr/lib64/ruby/gems/2.3.0/specifications/method_source-0.8.2.gemspec
