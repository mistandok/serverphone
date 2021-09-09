<p># serverphone<br />Примеры сервиса по стандартизации формата телефона, написанного на FastAPI</p>
<p>Сервисы размещены по URI-ссылкам:<br /><a href="https://mistandok.ru/unify_phone_from_json">https://mistandok.ru/unify_phone_from_json</a><br /><a href="https://mistandok.ru/unify_phone_from_form">https://mistandok.ru/unify_phone_from_form</a><br /><a href="https://mistandok.ru/unify_phone_from_query">https://mistandok.ru/unify_phone_from_query</a><br /><a href="https://mistandok.ru/unify_phone_from_cookies">https://mistandok.ru/unify_phone_from_cookies</a></p>
<p style="text-align: center;"><strong>1.&nbsp;unify_phone_from_json</strong></p>
<p>Сервис&nbsp;обрабатывает&nbsp;HTTP POST запросы и&nbsp;принимает телефон&nbsp;в теле запроса в виде JSON:</p>
<pre><code class="language-json hljs">{<span class="hljs-attr">"phone"</span>: <span class="hljs-string">"89013455678"</span>}</code><br /><br />Телефон приводится к виду: 8 (901) 345-56-78<br /><br /></pre>
<p style="text-align: center;"><strong>2.&nbsp;unify_phone_from_form</strong></p>
<p><span>Сервис&nbsp;обрабатывает&nbsp;HTTP POST запросы и&nbsp;принимает телефон&nbsp;в теле Form Data.</span><br />Телефон приводится к виду: 8 (901) 345-56-78<br /><br /></p>
<p style="text-align: center;"><strong>3.&nbsp;unify_phone_from_query</strong></p>
<p>Сервис&nbsp;обрабатывает&nbsp;HTTP GET запросы и&nbsp;принимает телефон&nbsp;в query параметре:</p>
<pre>https://mistandok.ru/unify_phone_from_query?phone=89001234523<br /><br />Телефон приводится к виду: <span>8 (900) 123-45-23</span><br /><br /></pre>
<p style="text-align: center;"><strong>4.&nbsp;unify_phone_from_cookies</strong></p>
<p><span>Сервис&nbsp;обрабатывает&nbsp;HTTP GET запросы и&nbsp;принимает телефон&nbsp;в Cookie записи&nbsp;</span><code>phone</code><br />Телефон приводится к виду: 8 (901) 345-56-78</p>
<p></p>
